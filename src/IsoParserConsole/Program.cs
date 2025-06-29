using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;

namespace IsoParserConsole;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 0)
        {
            Console.WriteLine("Usage: IsoParserConsole <hex message>");
            return;
        }

        string hex = args[0];
        var parser = new Iso8583Parser();
        var message = parser.Parse(hex);
        Console.WriteLine($"MTI: {message.Mti}");
        foreach (var field in message.Fields)
        {
            Console.WriteLine($"DE-{field.Key}: {field.Value}");
        }
    }
}

public record IsoMessage(string Mti, Dictionary<int, string> Fields);

public class Iso8583Parser
{
    private readonly Dictionary<int, FieldDef> _defs = new()
    {
        {2, new FieldDef(FieldType.LLVAR)},
        {3, new FieldDef(6)},
        {4, new FieldDef(12)},
        {6, new FieldDef(12)},
        {7, new FieldDef(10)},
        {10, new FieldDef(8)},
        {11, new FieldDef(6)},
        {12, new FieldDef(6)},
        {13, new FieldDef(4)},
        {15, new FieldDef(4)},
        {18, new FieldDef(4)},
        {22, new FieldDef(3)},
        {25, new FieldDef(2)},
        {28, new FieldDef(9)},
        {32, new FieldDef(FieldType.LLVAR)},
        {37, new FieldDef(12)},
        {38, new FieldDef(6)},
        {39, new FieldDef(2)},
        {41, new FieldDef(8, FieldEncoding.Ascii)},
        {42, new FieldDef(15, FieldEncoding.Ascii)},
        {43, new FieldDef(40, FieldEncoding.Ascii)},
        {49, new FieldDef(3)},
        {51, new FieldDef(3)},
        {54, new FieldDef(FieldType.LLVAR)},
        {61, new FieldDef(FieldType.LLVAR)},
        {63, new FieldDef(FieldType.LLVAR)},
        {102, new FieldDef(FieldType.LLVAR)},
        {111, new FieldDef(FieldType.LLLVAR)}
    };

    public IsoMessage Parse(string hex)
    {
        byte[] bytes = Convert.FromHexString(hex);
        int index = 0;

        // length prefix
        index += 2; // two bytes length
        string mti = ReadAscii(bytes, ref index, 4);

        ulong primaryBitmap = ReadBitmap(bytes, ref index);
        ulong? secondaryBitmap = null;
        if ((primaryBitmap & (1UL << 63)) != 0)
        {
            secondaryBitmap = ReadBitmap(bytes, ref index);
        }

        var fields = new Dictionary<int, string>();
        for (int bit = 2; bit <= 128; bit++)
        {
            bool present = bit <= 64
                ? ((primaryBitmap >> (64 - bit)) & 1) == 1
                : secondaryBitmap != null && (((secondaryBitmap.Value) >> (128 - bit)) & 1) == 1;

            if (!present) continue;
            if (!_defs.TryGetValue(bit, out var def))
            {
                throw new NotSupportedException($"Field {bit} not supported");
            }
            string value = def.Read(bytes, ref index);
            fields[bit] = value;
        }

        return new IsoMessage(mti, fields);
    }

    static ulong ReadBitmap(byte[] bytes, ref int index)
    {
        ulong value = 0;
        for (int i = 0; i < 8; i++)
        {
            value = (value << 8) | bytes[index++];
        }
        return value;
    }

    static string ReadAscii(byte[] bytes, ref int index, int length)
    {
        string s = System.Text.Encoding.ASCII.GetString(bytes, index, length);
        index += length;
        return s;
    }
}

public enum FieldType
{
    Fixed,
    LLVAR,
    LLLVAR
}

public enum FieldEncoding
{
    Numeric,
    Ascii
}

public class FieldDef
{
    public FieldType Type { get; }
    public int Length { get; }
    public FieldEncoding Encoding { get; }

    public FieldDef(int length, FieldEncoding encoding = FieldEncoding.Numeric)
    {
        Type = FieldType.Fixed;
        Length = length;
        Encoding = encoding;
    }

    public FieldDef(FieldType type, FieldEncoding encoding = FieldEncoding.Numeric)
    {
        Type = type;
        Encoding = encoding;
    }

    public string Read(byte[] bytes, ref int index)
    {
        int len = Length;
        if (Type == FieldType.LLVAR)
        {
            len = int.Parse(ReadAscii(bytes, ref index, 2), CultureInfo.InvariantCulture);
        }
        else if (Type == FieldType.LLLVAR)
        {
            len = int.Parse(ReadAscii(bytes, ref index, 3), CultureInfo.InvariantCulture);
        }

        string value = Encoding == FieldEncoding.Ascii
            ? ReadAscii(bytes, ref index, len)
            : System.Text.Encoding.ASCII.GetString(bytes, index, len);
        index += len;
        return value;
    }

    static string ReadAscii(byte[] bytes, ref int index, int length)
    {
        string s = System.Text.Encoding.ASCII.GetString(bytes, index, length);
        index += length;
        return s;
    }
}

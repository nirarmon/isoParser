using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using IsoParserConsole;
using Xunit;

public class ParserTests
{
    public static IEnumerable<object[]> SingleFieldCases => new List<object[]>
    {
        new object[]{2, "100194868736564"},
        new object[]{3, "000000"},
        new object[]{4, "000000050000"},
        new object[]{6, "000000050100"},
        new object[]{7, "0122132918"},
        new object[]{10, "61002000"},
        new object[]{11, "016372"},
        new object[]{12, "182918"},
        new object[]{13, "0122"},
        new object[]{15, "0122"},
        new object[]{18, "5541"},
        new object[]{22, "902"},
        new object[]{25, "00"},
        new object[]{28, "D00000000"},
        new object[]{32, "000000"},
        new object[]{37, "802213016372"},
        new object[]{41, "TERMID01"},
        new object[]{42, "CARD ACCEPTOR"},
        new object[]{43, "ACQUIRER NAME CITY NAME CAUSA".PadRight(40)},
        new object[]{49, "840"}
    };

    [Theory]
    [MemberData(nameof(SingleFieldCases))]
    public void ParseSingleField(int field, string value)
    {
        string hex = IsoMessageBuilder.Build("0200", (field, value));
        var parser = new Iso8583Parser();
        var msg = parser.Parse(hex);
        Assert.Equal("0200", msg.Mti);
        Assert.Single(msg.Fields);
        Assert.Equal(value, msg.Fields[field]);
    }

    [Fact]
    public void ParseExampleFromSpec()
    {
        string hex = IsoMessageBuilder.Build("0100",
            (2, "100194868736564"),
            (3, "000000"),
            (4, "000000050000"),
            (6, "000000050100"),
            (7, "0122132918"),
            (10, "61002000"),
            (11, "016372"),
            (12, "182918"),
            (13, "0122"),
            (15, "0122"),
            (18, "5541"),
            (22, "902"),
            (25, "00"),
            (28, "D00000000"),
            (32, "000000"),
            (37, "802213016372"),
            (41, "TERMID01"),
            (42, "CARD ACCEPTOR"),
            (43, "ACQUIRER NAME CITY NAME CAUSA"),
            (49, "840"),
            (51, "840"),
            (54, "0072840D000000000100"),
            (61, "0000000004020000"),
            (63, "0002 123456123456123 0 VISA"),
            (102, "100194868736564"),
            (111, " 123456123456123 00 000000 0000000000 000000000000 0000000000 00020000000000000000 00 0768892")
        );

        var parser = new Iso8583Parser();
        var msg = parser.Parse(hex);

        Assert.Equal("0100", msg.Mti);
        Assert.Equal("100194868736564", msg.Fields[2]);
        Assert.Equal("000000050000", msg.Fields[4]);
        Assert.Equal("802213016372", msg.Fields[37]);
        Assert.Equal("TERMID01", msg.Fields[41]);
        Assert.Equal("840", msg.Fields[51]);
        Assert.Equal("0002 123456123456123 0 VISA", msg.Fields[63]);
    }
}

static class IsoMessageBuilder
{
    private static readonly Dictionary<int, FieldDef> Defs = new()
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

    public static string Build(string mti, params (int field, string value)[] fields)
    {
        var ordered = fields.OrderBy(f => f.field).ToList();
        bool[] primary = new bool[64];
        bool[] secondary = new bool[64];
        bool needSecondary = ordered.Any(f => f.field > 64);
        foreach (var f in ordered)
        {
            if (f.field <= 64) primary[f.field - 1] = true; else secondary[f.field - 65] = true;
        }
        if (needSecondary) primary[0] = true;
        var bytes = new List<byte>();
        bytes.AddRange(Encoding.ASCII.GetBytes(mti));
        bytes.AddRange(ToBitmap(primary));
        if (needSecondary) bytes.AddRange(ToBitmap(secondary));
        foreach (var f in ordered)
        {
            var def = Defs[f.field];
            bytes.AddRange(Encode(def, f.value));
        }
        ushort len = (ushort)bytes.Count;
        bytes.Insert(0, (byte)(len >> 8));
        bytes.Insert(1, (byte)(len & 0xFF));
        return Convert.ToHexString(bytes.ToArray());
    }

    private static byte[] ToBitmap(bool[] bits)
    {
        byte[] data = new byte[8];
        for (int i = 0; i < 64; i++)
            if (bits[i]) data[i / 8] |= (byte)(1 << (7 - (i % 8)));
        return data;
    }

    private static byte[] Encode(FieldDef def, string value)
    {
        var list = new List<byte>();
        if (def.Type == FieldType.LLVAR) list.AddRange(Encoding.ASCII.GetBytes(value.Length.ToString("D2")));
        else if (def.Type == FieldType.LLLVAR) list.AddRange(Encoding.ASCII.GetBytes(value.Length.ToString("D3")));
        list.AddRange(Encoding.ASCII.GetBytes(value));
        return list.ToArray();
    }
}

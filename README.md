# isoParser

This repository includes a simple ISO 8583 parser implemented in C# targeting .NET 8.0.

The parser reads a hexadecimal representation of an ISO 8583 message and outputs the message type and present data elements.

## Building

The project is contained in the `src` folder. To build or run the parser you need the .NET 8 SDK installed.

```
dotnet build src/IsoParser.sln
```

## Usage

Provide a hex string as an argument:

```
dotnet run --project src/IsoParserConsole -- <hex string>
```

The program will print the MTI and each parsed field.

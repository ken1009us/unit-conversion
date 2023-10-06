# Units Conversion System

## Prerequisites
- Python
- Required packages: grpcio, grpcio-tools, pint, json, re

## Installation

1. Clone this repository:
```bash
$ git clone https://github.com/ken1009us/unit-conversion.git
```

2. Navigate to the project directory:

```bash
$ cd unit-conversion
```

3. Install the required packages:
```bash
$ pip install -r requirements.txt
```

## Usage

Start the gRPC server:

```bash
$ cd units_grpc_server
$ python server.py
```

In a new terminal, use the client script to convert units:

```bash
$ cd tests
$ python client.py
```

## Custom Units

To add custom units, modify the conversions.json file in the config directory. The server will load these custom units on startup.

Example conversions.json:

```json
{
    "miG": "G/1024",
    "2miG": "G/512"
}
```

## Files

- server.py: The gRPC server script that handles unit conversion requests.
- client.py: A client script to test the gRPC server.
- units_core/: A directory containing the core unit conversion logic.
- units_proto/: Contains the Protocol Buffers and gRPC service definitions.
- config/conversions.json: A JSON file for defining custom units.

## Testing

Run the tests using pytest:

```bash
$ pytest unit-conversion
```

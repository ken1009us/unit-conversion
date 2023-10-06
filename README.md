# Units Conversion Service

The Unit Conversion Service is a sophisticated, user-friendly, and efficient software solution designed to facilitate seamless and accurate conversions between various units of measurement. This project is meticulously crafted to cater to the needs of engineers, scientists, students, and professionals who frequently encounter the necessity to convert units in their daily tasks or complex projects.

## Technology Integration

- gRPC Protocol: Utilize gRPC for efficient, fast, and reliable communication between clients and servers.
- Pint Library: Leverage the Pint library for handling unit conversions, ensuring a robust and reliable conversion mechanism.

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

## Acknowledgements

### Project Origin

This is an open source project initiated at PhysIQ. The objective was to develop a comprehensive unit conversion service that is versatile, efficient, and user-friendly.

### Personal Contribution
I took the initiative to enhance and complete the project independently. These efforts were aimed at optimizing the service’s performance, extending its functionality, and ensuring its adaptability to diverse unit conversion needs.

### Disclaimer
This project is a new version of the original code and does not represent the entirety of the work done at PhysIQ. It is a demonstration of my individual contributions and enhancements made to improve the project's functionality and performance.
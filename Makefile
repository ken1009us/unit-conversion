.PHONY: all generate-proto generate-grpc

all: generate-proto generate-grpc

generate-proto:
	protoc -I=. --python_out=. units_proto/units.proto units_grpc_stub/conversion_service.proto

generate-grpc:
	python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. units_grpc_stub/conversion_service.proto
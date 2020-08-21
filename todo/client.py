import grpc

import proto.server_pb2 as models
from proto.server_pb2_grpc import TodoServerStub

channel = grpc.insecure_channel("localhost:8000")
stub = TodoServerStub(channel)

print("Check current lists")
result = stub.GetLists(models.Empty())
print(result.lists)

print("Create a new list")
result = stub.CreateList(models.CreateListRequest(name="bob"))
print(result)

print("Check current lists")
result = stub.GetLists(models.Empty())
print(result.lists)

print("Checking a list")
result = stub.GetList(models.GetListRequest(name="bob"))
print(result.items)

print("Add item to a list")
result = stub.AddToList(models.AddToListRequest(list_name="bob", value="Clean bob"))
print(result)

print("Check all lists")
result = stub.GetLists(models.Empty())
print(result.lists)

print("Add item to a non-existent list")
try:
    result = stub.AddToList(
        models.AddToListRequest(list_name="bobby", value="Clean bob")
    )
except grpc.RpcError as e:
    print(e.code())

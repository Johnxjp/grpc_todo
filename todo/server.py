from concurrent import futures
from dataclasses import dataclass
from enum import Enum
from uuid import uuid4

import grpc

from proto import server_pb2 as models
from proto import server_pb2_grpc
from proto.server_pb2_grpc import TodoServerServicer


class ItemStatus(Enum):
    INCOMPLETE = 0
    COMPLETE = 1


@dataclass
class Item:
    id: uuid4
    value: str
    status: ItemStatus = ItemStatus.INCOMPLETE


def grpc_to_item(request_item: models.Item) -> Item:
    item = Item(request_item.item_id, request_item.value)
    status = (
        ItemStatus.COMPLETE
        if request_item.status == models.ItemStatus.COMPLETE
        else ItemStatus.INCOMPLETE
    )
    item.status = status
    return item


def item_to_grpc(item: Item) -> models.Item:
    return models.Item(item_id=str(item.id), value=item.value, status=item.status.value)


class TodoServer(TodoServerServicer):
    def __init__(self):
        self.todo_lists = {}

    def CreateList(
        self, request: models.CreateListRequest, context: grpc.ServicerContext
    ) -> models.Empty:
        name = request.name
        if not name:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "List name cannot be empty")

        if name in self.todo_lists:
            context.abort(grpc.StatusCode.ALREADY_EXISTS, "List already exists.")

        self.todo_lists[name] = {}
        return models.Empty()

    def AddToList(
        self, request: models.AddToListRequest, context: grpc.ServicerContext
    ) -> models.Item:
        items = self.todo_lists.get(request.list_name, None)
        if items is None:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "List does not exist")

        item_id = uuid4()
        item = Item(item_id, request.value, ItemStatus.COMPLETE)
        self.todo_lists[request.list_name][item_id] = item
        return models.Item(
            item_id=str(item.id), value=item.value, status=item.status.value
        )

    def UpdateItemStatus(
        self, request: models.UpdateItemStatusRequest, context: grpc.ServicerContext
    ) -> models.Item:
        list_name = request.list_name
        items = self.todo_lists.get(list_name, None)
        if items is None:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "List does not exist")

        item_id = request.item.item_id
        if items.get(item_id, None) is None:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Item does not exist")

        updated_item = grpc_to_item(request.item)
        items[item_id] = updated_item
        return models.Item(
            item_id=str(updated_item.id),
            value=updated_item.value,
            status=updated_item.status,
        )

    def GetLists(
        self, request: models.Empty, context: grpc.ServicerContext
    ) -> models.GetListsResponse:
        lists = [
            models.List(
                name=name, items=[item_to_grpc(item) for item in items.values()]
            )
            for name, items in self.todo_lists.items()
        ]
        return models.GetListsResponse(lists=lists)

    def GetList(
        self, request: models.GetListRequest, context: grpc.ServicerContext
    ) -> models.GetListResponse:
        items = self.todo_lists.get(request.name, [])
        return models.GetListResponse(items=[models.Item(item=item) for item in items])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    server_pb2_grpc.add_TodoServerServicer_to_server(TodoServer(), server)
    server.add_insecure_port("[::]:8000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    print("Starting server")
    serve()

import uuid
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from sockets.socket_manager import SocketManager

router = APIRouter()
socket_manager = SocketManager()


@router.websocket("/connect")
async def connect(socket: WebSocket):
    client_id = str(uuid.uuid4())

    await socket_manager.connect(socket, client_id)

    try:
        await socket.send_json(
            {"client_id": client_id, "message": "Client is connected!"}
        )

        while True:
            data = await socket.receive_json()
            event = data.get("event")

    except WebSocketDisconnect:
        socket_manager.disconnect(client_id)
        await socket_manager.send_message("Connection lost!")

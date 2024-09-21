# FastAPI
from fastapi import FastAPI
from fastapi import WebSocket, WebSocketDisconnect

# Src
from src.manager import WebSocketManager

# Router
from routers.users import UserRouter

app = FastAPI()
manager = WebSocketManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while manager.is_active(websocket):
            data = await websocket.receive_text()
            print(data)
    except WebSocketDisconnect:
        ...
    manager.disconnect(websocket)

app.include_router(UserRouter())
# Typing
from typing import List

# FastAPI
from fastapi import WebSocket

class WebSocketManager:

    def __init__(self):
        self._active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self._active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self._active_connections.remove(websocket)

    def is_active(self, websocket: WebSocket) -> bool:
        return websocket in self._active_connections
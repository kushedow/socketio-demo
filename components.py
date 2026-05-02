import socketio
from fastapi import FastAPI
fast_app = FastAPI()

sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")
app = socketio.ASGIApp(sio, other_asgi_app=fast_app)

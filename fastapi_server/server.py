from fastapi import FastAPI
from fastapi_socketio import SocketManager
from loguru import logger
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="../public"), name="static")
socket_manager = SocketManager(app=app, mount_location="/ws")


connected_users = []


@app.sio.on("connect")
async def connect(sid, environ):
    """Handle initial connection of socket user."""
    connected_users.append(sid)
    logger.info(f"User {sid} connected")


@app.sio.on("disconnect")
async def disconnect(sid):
    """Handle disconnection."""
    connected_users.remove(sid)
    await app.sio.emit("update-user-list", {"userIds": connected_users})
    logger.info(f"User {sid} disconnected")


@app.sio.on("requestUserList")
async def request_user_list(sid):
    """Update list of users."""
    await app.sio.emit("update-user-list", {"userIds": connected_users})
    logger.info(f"{sid} requested user list update")


@app.sio.on("mediaOffer")
async def media_offer(sid, data):
    """Handle offer to communicate."""
    await app.sio.emit(
        "mediaOffer", {"from": data["from"], "offer": data["offer"]}, room=data["to"]
    )
    logger.info(f"Media Offer from {data['from']}")


@app.sio.on("mediaAnswer")
async def media_answer(sid, data):
    """Handle media answer."""
    await app.sio.emit(
        "mediaAnswer", {"from": data["from"], "answer": data["answer"]}, room=data["to"]
    )
    logger.info(f"Media Answer from {data['from']}")


@app.sio.on("iceCandidate")
async def ice_candidate(sid, data):
    """Handle Ice Candidate."""
    await app.sio.emit(
        "remotePeerIceCandidate", {"candidate": data["candidate"]}, room=data["to"]
    )
    logger.info(f"Ice candidate for  {data['to']}")


@app.get("/")
def read_root():
    return FileResponse("../public/index.html")

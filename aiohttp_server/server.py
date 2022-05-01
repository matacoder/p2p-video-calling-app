from aiohttp import web
import socketio
from loguru import logger

sio = socketio.AsyncServer(async_mode="aiohttp")
app = web.Application()
sio.attach(app)

connected_users = []


async def index(request):
    """Serve the client-side application."""
    with open("/app/public/index.html") as f:
        return web.Response(text=f.read(), content_type="text/html")


@sio.event
async def connect(sid, environ):
    """Handle initial connection of socket user."""
    connected_users.append(sid)
    logger.info(f"User {sid} connected")


@sio.event
async def disconnect(sid):
    """Handle disconnection."""
    connected_users.remove(sid)
    await sio.emit("update-user-list", {"userIds": connected_users})
    logger.info(f"User {sid} disconnected")


@sio.on("requestUserList")
async def request_user_list(sid):
    """Update list of users."""
    await sio.emit("update-user-list", {"userIds": connected_users})
    logger.info(f"{sid} requested user list update")


@sio.on("mediaOffer")
async def media_offer(sid, data):
    """Handle offer to communicate."""
    await sio.emit(
        "mediaOffer", {"from": data["from"], "offer": data["offer"]}, room=data["to"]
    )
    logger.info(f"Media Offer from {data['from']}")


@sio.on("mediaAnswer")
async def media_answer(sid, data):
    """Handle media answer."""
    await sio.emit(
        "mediaAnswer", {"from": data["from"], "answer": data["answer"]}, room=data["to"]
    )
    logger.info(f"Media Answer from {data['from']}")


@sio.on("iceCandidate")
async def ice_candidate(sid, data):
    """Handle Ice Candidate."""
    await sio.emit(
        "remotePeerIceCandidate", {"candidate": data["candidate"]}, room=data["to"]
    )
    logger.info(f"Ice candidate for  {data['to']}")


app.router.add_static("/static", "/app/public")
app.router.add_get("/", index)

if __name__ == "__main__":
    web.run_app(app, port=3000)

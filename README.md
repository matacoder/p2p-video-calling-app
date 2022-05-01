# WebRTC Peer to Peer Video Calls

<img src="https://github.com/matacoder/p2p-video-calling-app/raw/master/public/webrtc.png">

Proof of concept for peer to peer calls using WebRTC technology.

There are two servers:
- JavaScript (Node.JS Express)
- Python (AIOHTTP)

## Environment

Please use your host in [line 11](public/index.css) instead of:
`const socket = io('https://call.matakov.com');` or just `http://localhost:3000` to run locally. Plan to use here environment variable.

## Docker Compose installation

Just run `docker compose -f docker-compose-aiohttp.yaml up --build -d` to start video app, it would be available at [http://localhost:3000](http://localhost:3000)

Or `docker compose -f docker-compose-fastapi.yaml up --build -d` if you want to use FastAPI

## JavaScript installation

Just run `docker compose -f docker-compose-nodejs.yaml up --build -d` to start video app, it would be available at [http://localhost:3000](http://localhost:3000)

To run the app without docker:

`yarn && yarn dev`
 
 or if you use npm:
 
`npm i && npm run dev`
 
 Once the server is running, open [http://localhost:3000](http://localhost:3000) in 2 separate tabs in your favourite browser.
 
 Select ID of the user and click call.

## Links

- [Official site of WebRTC](https://webrtc.github.io/)
- [AIOHTTP Socket.IO](https://python-socketio.readthedocs.io/en/latest/server.html#aiohttp)
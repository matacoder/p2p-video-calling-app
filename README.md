# WebRTC Peer to Peer Video Calls

Proof of concept for peer to peer calls using WebRTC technology.

For now client and server side is implemented in JavaScript.

Planning to rewrite server side with `FastAPI` python framework.

## Environment

Please use your host in [line 11](public/index.css) instead of:
`const socket = io('https://call.matakov.com');` or just `http://localhost:3000` to run locally. Plan to use here environment variable.

## Docker Compose installation

Just run `docker compose up -d` to start video app, it would be available at [http://localhost:3000](http://localhost:3000)

## JavaScript installation

To run the example:

`yarn && yarn dev`
 
 or if you use npm:
 
 `npm i && npm run dev`
 
 Once the server is running, open [http://localhost:3000](http://localhost:3000) in 2 separate tabs in your favourite browser.
 
 Select ID of the user and click call.

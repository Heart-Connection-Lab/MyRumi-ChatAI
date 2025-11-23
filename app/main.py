from fastapi import FastAPI
from app.api.rest.health import router as health_router
from app.api.websocket import router as websocket_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MyRumi Backend Running"}

# Health Check
app.include_router(health_router)

# WebSocket
app.include_router(websocket_router)
from fastapi import FastAPI
from app.api.rest.health import router as health_router
from app.api.websocket import router as websocket_router
from app.api.rest.graph_test import router as graph_test_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "MyRumi Backend Running"}

# Health Check
app.include_router(health_router)

# WebSocket
app.include_router(websocket_router)

# LangGraph Test
app.include_router(graph_test_router)
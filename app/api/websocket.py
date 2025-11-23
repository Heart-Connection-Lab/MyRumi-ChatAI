from fastapi import APIRouter, WebSocket, WebSocketDisconnect

router = APIRouter(prefix="/ws", tags=["websocket"])


@router.websocket("/connect")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("🔌 WebSocket 연결됨")

    try:
        while True:
            # 클라이언트가 보낸 메시지 받기
            data = await websocket.receive_text()
            print(f"📩 받은 데이터: {data}")

            # 그대로 echo 해서 돌려보냄
            await websocket.send_text(f"echo: {data}")

    except WebSocketDisconnect:
        print("❌ WebSocket 연결 끊김")

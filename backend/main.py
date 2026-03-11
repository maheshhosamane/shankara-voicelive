from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import httpx

app = FastAPI()

# Azure endpoints
activity_protocol_url = "https://AIResourceGroupMH.services.ai.azure.com/api/projects/Proj-Companion/applications/Shankara/protocols/activityprotocol?api-version=2025-11-15-preview"
response_api_url = "https://AIResourceGroupMH.services.ai.azure.com/api/projects/Proj-Companion/applications/Shankara/protocols/openai/responses?api-version=2025-11-15-preview"

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Receive a message from the WebSocket
            message = await websocket.receive_text()
            # Forward the message to Activity Protocol
            async with httpx.AsyncClient() as client:
                response = await client.post(activity_protocol_url, json={'message': message})
                response.raise_for_status()
                await websocket.send_text(response.text)
    except WebSocketDisconnect:
        print("Client disconnected")
    except httpx.HTTPStatusError as exc:
        await websocket.send_text(f"Error: {exc.response.text}")
    except Exception as e:
        await websocket.send_text(f"Unexpected error: {str(e)}")

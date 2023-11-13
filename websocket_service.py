# websocket_service.py

from nameko.rpc import rpc

class WebSocketService:
    name = "websocket_service"

    connected_clients = set()

    @rpc
    def notify_user(self, user_id, message):
        # Logic to send real-time updates to a specific user
        for client_id in self.connected_clients:
            if client_id == user_id:
                self.send_update(client_id, message)

    @rpc
    def connect(self, user_id):
        # Logic to handle WebSocket connection
        self.connected_clients.add(user_id)
        print(f"WebSocket connected for user: {user_id}")

    @rpc
    def disconnect(self, user_id):
        # Logic to handle WebSocket disconnection
        self.connected_clients.remove(user_id)
        print(f"WebSocket disconnected for user: {user_id}")

    def send_update(self, user_id, message):
        # Helper method to send updates via WebSocket
        return {"user_id": user_id, "message": message}

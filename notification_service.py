
from nameko.rpc import rpc
from nameko.rpc import RpcProxy
from nameko.timer import timer

class NotificationService:
    name = "notification_service"

    @rpc
    def send_notification(self, user_id, message):
        # Logic to send notifications (e.g., push notifications, emails)
        # Implement the actual notification mechanism based on your requirements
        print(f"Sending notification to {user_id}: {message}")

    websocket_service = RpcProxy("websocket_service")
    database_service = RpcProxy("database_service")

    @timer(interval=10)
    def send_periodic_notification(self):
        # Simulate periodic notifications
        user_id = "user123"
        message = "New update!"

        # Notify user via WebSocket
        self.websocket_service.notify_user(user_id, message)

        # Save noti
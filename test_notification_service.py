# test_notification_service.py

from nameko.testing.services import worker_factory
from notification_service import NotificationService

def test_send_notification():
    service = worker_factory(NotificationService)

    # Mock the WebSocketService and DatabaseService calls
    service.websocket_service.notify_user = lambda user_id, message: None
    service.database_service.save_notification = lambda user_id, message: None

    # Call the method to be tested
    service.send_notification("user123", "Test message")

    # Add assertions based on your logic

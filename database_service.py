# database_service.py

from nameko.rpc import rpc
from pymongo import MongoClient

class DatabaseService:
    name = "database_service"

    client = MongoClient("mongodb://localhost:27017/")
    db = client.notification_db

    @rpc
    def save_notification(self, user_id, message):
        # Logic to save notifications in the database
        self.db.notifications.insert_one({"user_id": user_id, "message": message})

    @rpc
    def get_notifications(self, user_id):
        # Logic to retrieve user-specific notifications from the database
        notifications = self.db.notifications.find({"user_id": user_id})
        return [notification["message"] for notification in notifications]

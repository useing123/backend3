from datetime import datetime

from bson.objectid import ObjectId
from pymongo.database import Database

from ..utils.security import hash_password


class AuthRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_user(self, user: dict):
        payload = {
            "email": user["email"],
            "password": hash_password(user["password"]),
            "created_at": datetime.utcnow(),
        }

        self.database["users"].insert_one(payload)

    def get_user_by_id(self, user_id: str) -> dict | None:
        user = self.database["users"].find_one(
            {
                "_id": ObjectId(user_id),
            }
        )
        return user

    def get_user_by_email(self, email: str) -> dict | None:
        user = self.database["users"].find_one(
            {
                "email": email,
            }
        )
        return user

    def update_user_data(self, user_id: str, updated_data: dict) -> None:
        payload = {
            "phone": updated_data.get("phone"),
            "name": updated_data.get("name"),
            "city": updated_data.get("city"),
        }
        self.database["users"].update_one(
            {
                "_id": ObjectId(user_id),
            },
            {"$set": payload},
        )


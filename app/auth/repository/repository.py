from datetime import datetime
from bson.objectid import ObjectId
from pymongo.database import Database
from bson import ObjectId
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
        
    def create_shanyrak(self, data: dict) -> str:
        payload = {
            "type": data["type"],
            "price": data["price"],
            "address": data["address"],
            "area": data["area"],
            "rooms_count": data["rooms_count"],
            "description": data["description"],
        }
        result = self.database["shanyraks"].insert_one(payload)
        ad_id = str(result.inserted_id)
        return ad_id

    def get_advertisement_by_id(self, ad_id: str) -> dict | None:
        ad = self.database["shanyraks"].find_one(
            {
                "_id": ObjectId(ad_id),
            }
        )
        return ad

    def update_advertisement_data(self, ad_id: str, updated_data: dict) -> None:
        payload = {
            "type": updated_data.get("type"),
            "price": updated_data.get("price"),
            "address": updated_data.get("address"),
            "area": updated_data.get("area"),
            "rooms_count": updated_data.get("rooms_count"),
            "description": updated_data.get("description"),
        }
        self.database["shanyraks"].update_one(
            {
                "_id": ObjectId(ad_id),
            },
            {"$set": payload},
        )

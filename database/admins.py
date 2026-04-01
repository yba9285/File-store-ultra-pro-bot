from .connection import db
from config import OWNER_ID

col = db.admins

async def add_admin(user_id: int):
    await col.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id}},
        upsert=True
    )

async def remove_admin(user_id: int):
    await col.delete_one({"user_id": user_id})

async def is_admin(user_id: int):
    if user_id == OWNER_ID:
        return True

    return await col.find_one({"user_id": user_id}) is not None

async def get_all_admins():
    return col.find({})

async def count_admins():
    return await col.count_documents({})

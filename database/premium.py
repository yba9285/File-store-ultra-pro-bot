from datetime import datetime, timedelta
from .connection import db

col = db.premium


async def add_premium(user_id: int, days: int):
    expiry_date = datetime.utcnow() + timedelta(days=days)

    await col.update_one(
        {"user_id": user_id},
        {"$set": {"expiry": expiry_date}},
        upsert=True
    )


async def remove_premium(user_id: int):
    await col.delete_one({"user_id": user_id})


async def is_premium(user_id: int):
    user = await col.find_one({"user_id": user_id})
    if not user:
        return False

    return user["expiry"] > datetime.utcnow()


async def get_premium_users():
    return await col.find({}).to_list(length=None)


# ✅ ADD THIS (so web/routes.py works)
async def get_all_premium():
    return await col.find({}).to_list(length=None)

async def count_premium_users():
    return await col.count_documents({})

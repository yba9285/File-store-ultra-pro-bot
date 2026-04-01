from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client(
    "FileStoreBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

if __name__ == "__main__":
    app.start()
    print("Bot Started ✅")

    import asyncio
    asyncio.get_event_loop().run_forever()

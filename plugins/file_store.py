from pyrogram import Client, filters
from config import WEB_URL, DB_CHANNEL
from database.files import save_file
from database.logs import add_log
from middleware.rate_limit import check_rate_limit


@Client.on_message(filters.document | filters.video | filters.audio)
async def store_file(client, message):

    if not await check_rate_limit(message.from_user.id):
        return

    file = message.document or message.video or message.audio

    # 🔥 STEP 1: File ko DB_CHANNEL me copy karo
    sent = await client.copy_message(
        DB_CHANNEL,
        message.chat.id,
        message.id
    )

    # 🔥 STEP 2: Message ID save karo (NOT file_id)
    await save_file(
        str(sent.id),  # ⚠️ IMPORTANT FIX
        file.file_name,
        message.from_user.id
    )

    # 🔹 Logging same rakha (no change)
    await add_log(
        action="file_upload",
        user_id=message.from_user.id,
        extra={"file_name": file.file_name}
    )

    # 🔥 STEP 3: Correct link generate
    link = f"{WEB_URL}/file/{sent.id}"

    await message.reply(
        f"✅ File Stored Successfully!\n\n🔗 {link}"
    )

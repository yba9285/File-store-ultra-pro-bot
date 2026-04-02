from pyrogram import Client, filters
from config import WEB_URL, DB_CHANNEL
from database.files import save_file
from database.logs import add_log
from middleware.rate_limit import check_rate_limit


@Client.on_message(filters.document | filters.video | filters.audio)
async def store_file(client, message):
    # ✅ Safe check for message.from_user
    user = message.from_user
    if user is None:
        # System message / anonymous post → ignore
        return

    user_id = user.id

    # ✅ Rate limit check
    if not await check_rate_limit(user_id):
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
        user_id
    )

    # 🔹 Logging same rakha (no change)
    await add_log(
        action="file_upload",
        user_id=user_id,
        extra={"file_name": file.file_name}
    )

    # 🔥 STEP 3: Correct link generate
    link = f"{WEB_URL}/file/{sent.id}"

    await message.reply(
        f"✅ File Stored Successfully!\n\n🔗 {link}"
    )

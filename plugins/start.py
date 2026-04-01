from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo,
    CallbackQuery
)

from config import WEB_URL, START_PHOTO, OWNER_USERNAME
from database.users import add_user
from middleware.force_sub import check_force
from middleware.rate_limit import check_rate_limit


# 🔹 START COMMAND
@Client.on_message(filters.command("start"))
async def start_handler(client, message):

    user_id = message.from_user.id

    # Rate Limit Protection
    if not await check_rate_limit(user_id):
        return

    # Save user
    await add_user(user_id)

    # Force Subscribe Check
    if not await check_force(client, user_id):
        await message.reply(
            "🚫 You must join the required channel before using this bot."
        )
        return

    caption = (
        "🚀 **Welcome to Advanced File Store Bot**\n\n"
        "This bot allows you to:\n\n"
        "📂 Store unlimited files\n"
        "🔗 Generate secure direct links\n"
        "🌐 Stream media instantly\n"
        "👑 Full admin web control panel\n"
        "⚡ Fast & secure file delivery\n\n"
        "Use the button below to open the control panel."
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "⚙️ Open Control Panel",
                web_app=WebAppInfo(url=WEB_URL)
            )
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about_bot"),
            InlineKeyboardButton("❌ Close", callback_data="close_msg")
        ]
    ])

    await message.reply_photo(
        photo=START_PHOTO,
        caption=caption,
        reply_markup=keyboard
    )


# 🔹 ABOUT BUTTON
@Client.on_callback_query(filters.regex("about_bot"))
async def about_callback(client, query: CallbackQuery):

    text = (
        "🤖 **About This Bot**\n\n"
        "Owner: @{owner}\n\n"
        "🖥 Deploy Platforms Supported:\n"
        "• VPS (Recommended)\n"
        "• Railway\n"
        "• Render\n"
        "• Koyeb\n"
        "• Docker\n\n"
        "Built with Pyrogram & Flask.\n"
        "Production ready architecture."
    ).format(owner=OWNER_USERNAME)

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("🔙 Back", callback_data="back_start")
        ]
    ])

    await query.message.edit_caption(
        caption=text,
        reply_markup=keyboard
    )


# 🔹 BACK BUTTON
@Client.on_callback_query(filters.regex("back_start"))
async def back_to_start(client, query: CallbackQuery):

    caption = (
        "🚀 **Welcome to Advanced File Store Bot**\n\n"
        "📂 Store unlimited files\n"
        "🔗 Generate secure direct links\n"
        "🌐 Stream media instantly\n"
        "👑 Full admin web control panel\n\n"
        "Open control panel below."
    )

    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "⚙️ Open Control Panel",
                web_app=WebAppInfo(url=WEB_URL)
            )
        ],
        [
            InlineKeyboardButton("ℹ️ About", callback_data="about_bot"),
            InlineKeyboardButton("❌ Close", callback_data="close_msg")
        ]
    ])

    await query.message.edit_caption(
        caption=caption,
        reply_markup=keyboard
    )


# 🔹 CLOSE BUTTON
@Client.on_callback_query(filters.regex("close_msg"))
async def close_message(client, query: CallbackQuery):
    await query.message.delete()

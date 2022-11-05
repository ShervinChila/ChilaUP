#(©)CrowdShot

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🧛 سازنده : شـروین\n🏠 خونه زندگیم : <a href='https://t.me/irbollywoodorg1/'>چنل ایران بالیوود </a>\n👧🏻 حرف و حدیثی با ما : رئیس کوچولو فعلا آیدی نداره بذاریم </a>\n🌏 وبسایت ما : در حال ساخت </b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("برگشت", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass

import logging
import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    name = user.first_name if user else "there"
    await update.message.reply_text(
        f"Hi {name}! I'm your Python Telegram bot.\n\n"
        "Send /ajio to get the AJIO loot trick."
    )


AJIO_MESSAGE = (
    "🔥 AJIO Loot Trick 🔥 Get ₹200 Shopping at Just ₹59 (Only for New Users)\n\n"
    "💥 Download App: https://ajioapps.onelink.me/2ic3/welcometoajio\n\n"
    "🎯 Referral Code: DHRFKFGPC\n\n"
    "🛒 Add items worth minimum ₹200 to your cart\n"
    "🏷 Apply Code: NEW30\n"
    "➕ Use ₹100 wallet balance\n\n"
    "✅ Final Payment: Only ₹59\n\n"
    "🛍 Product Link: https://ajiio.in/OJcBA3J"
)


async def ajio_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(AJIO_MESSAGE, disable_web_page_preview=False)


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    logger.error("Exception while handling an update:", exc_info=context.error)


def main() -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN is not set. Add it via Replit Secrets."
        )

    app = Application.builder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ajio", ajio_command))
    app.add_error_handler(error_handler)

    logger.info("Bot starting (long polling)...")
    app.run_polling(allowed_updates=Update.ALL_TYPES, drop_pending_updates=True)


if __name__ == "__main__":
    main()

import telegram
import asyncio

bot_token = "7171868311:AAFKK98ywDcc9miItSTGm99T7pweM6oP4ZY"
chat_id = "7787352867"

bot = telegram.Bot(token=bot_token)
message = "Test!"
bot.send_message(chat_id=chat_id, text=message)  # Use await here!


async def send_telegram_message(bot_token, chat_id, message):  # Define an async function
    try:
        bot = telegram.Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=message)  # Use await here!
        print("Telegram message sent!")
    except Exception as e:
        print(f"Error sending Telegram message: {type(e).__name__}: {e}")  # Print full error

# The correct way to run an async function from a regular function:
# asyncio.run(send_telegram_message(bot_token, chat_id, message))


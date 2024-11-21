# 1. Set Up Your Telegram Bot
Contact BotFather:
Open Telegram and search for BotFather.
Start a chat with BotFather and use the /newbot command.
Follow the instructions to name your bot and get your bot token.
Save Your Bot Token:
BotFather will provide you with a token (a string like 123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11).
Keep this token secure—it’s your bot’s key to the Telegram API.
# 2. Set Up ChatGPT API Access
Get OpenAI API Key:
Sign up at OpenAI if you haven’t already.
Go to your OpenAI API settings and create an API key.
Save this key; you’ll need it to interact with ChatGPT.
Choose a Programming Language:
Use a language like Python for its simplicity and strong library support.
3. Install Required Libraries
In your development environment, install the necessary Python libraries:

pip install python-telegram-bot openai
4. Write the Bot Code
Create a Python script (e.g., telegram_chatgpt_bot.py) with the following content:

import openai
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your API keys
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

openai.api_key = OPENAI_API_KEY

# Function to handle user messages
def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    chat_id = update.message.chat_id

    try:
        # Send the user's message to ChatGPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ],
        )

        # Extract ChatGPT's response
        bot_reply = response['choices'][0]['message']['content']

        # Send the reply back to Telegram
        update.message.reply_text(bot_reply)
    except Exception as e:
        update.message.reply_text("Something went wrong. Please try again later.")
        print(e)

# Start command handler
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi! I'm your AI bot. How can I assist you today?")

# Main function to run the bot
def main():
    # Set up the Telegram bot
    updater = Updater(TELEGRAM_BOT_TOKEN)

    # Register handlers
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
5. Run the Bot
Save the script and run it using Python:
python telegram_chatgpt_bot.py
Your bot will now be active and listening for messages on Telegram.
6. Test the Bot
Go to Telegram, find your bot, and start a chat.
Send messages, and your bot should reply using ChatGPT!

import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Your API keys
TELEGRAM_BOT_TOKEN = ""
OPENAI_API_KEY = ""

# Configure OpenAI API
openai.api_key = OPENAI_API_KEY

# Handle /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles the /start command."""
    await update.message.reply_text(
        "Hello! I'm your AI-powered assistant. You can ask me anything, whether it's a question, a task, or a problem you'd like solved. How can I help you today?"
    )

# Handle user messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handles incoming messages and forwards them to OpenAI for response."""
    user_message = update.message.text

    try:
        # Make an API call to OpenAI for chat-based completion
        response = await openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Using GPT-3.5 model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message},
            ]
        )

        # Extract the assistant's response from the OpenAI API response
        bot_reply = response['choices'][0]['message']['content']

        # Send the response to the user
        await update.message.reply_text(bot_reply)

    except Exception as e:
        # Handle errors gracefully
        print(f"Error occurred: {e}")
        await update.message.reply_text("Sorry, an error occurred while processing your request. Please try again later.")

# Main function to run the bot
def main():
    """Sets up and starts the bot."""
    # Initialize the application with the bot token
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Add handlers for commands and messages
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot with polling
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
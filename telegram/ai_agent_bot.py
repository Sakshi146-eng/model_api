import telebot
import time
import random
import openai


# Initialize the bot with your token from BotFather
# Replace 'YOUR_BOT_TOKEN' with the token you received from @BotFather
bot = telebot.TeleBot("YOUR_BOT_TOKEN")


def get_ai_response(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

# Handler for /start and /help commands
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    Respond to start/help commands with introduction
    """
    welcome_text = (
        f"Hello {message.from_user.first_name}! 👋\n\n"
        "I'm your AI agent bot. I can have simple conversations with you.\n"
        "Try saying hello, asking how I am, or just chat with me!\n\n"
        "This is a real-time communication test."
    )
    bot.reply_to(message, welcome_text)

# Handler for all text messages
@bot.message_handler(func=lambda message: True)
def echo_and_respond(message):
    """
    Main message handler - processes all incoming messages
    """
    try:
        # Show typing indicator for better UX
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Simulate AI processing time (remove in production)
        time.sleep(1)
        
        # Get AI-generated response
        ai_response = get_ai_response(message.text)
        
        # Send the response
        bot.reply_to(message, f"You said: {message.text}\n\n🤖 AI Agent: {ai_response}")
        
        # Log the interaction
        print(f"User {message.from_user.username} ({message.chat.id}): {message.text}")
        print(f"Bot response: {ai_response}\n")
        
    except Exception as e:
        print(f"Error processing message: {e}")
        bot.reply_to(message, "Sorry, I encountered an error processing your message.")

# Handler for non-text messages (photos, documents, etc.)
@bot.message_handler(content_types=['photo', 'document', 'audio', 'video', 'sticker'])
def handle_media(message):
    """
    Respond to media messages appropriately
    """
    bot.reply_to(message, "I can only process text messages right now, but I appreciate you sharing!")

# Handler for when the bot starts
@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
def on_user_joins(message):
    """
    Welcome new users when they first interact
    """
    for new_member in message.new_chat_members:
        if new_member.id == bot.get_me().id:
            # Bot joined a group
            bot.reply_to(message, "Thanks for adding me! Use /start to begin.")
            break

# Error handler
@bot.message_handler(func=lambda message: True, content_types=['text'])
def error_handler(message):
    """
    Catch and handle any unexpected errors
    """
    try:
        # Your main handlers should cover this, but just in case
        pass
    except Exception as e:
        print(f"Unhandled error: {e}")
        bot.reply_to(message, "An unexpected error occurred. Please try again.")

def start_bot():
    """
    Main function to start the bot with retry logic
    """
    print("Starting AI Agent Bot...")
    print("Bot is running. Press Ctrl+C to stop.")
    print("-" * 50)
    
    while True:
        try:
            # Start polling for messages (real-time communication)
            bot.infinity_polling(timeout=60, long_polling_timeout=30)
        except Exception as e:
            print(f"Connection error: {e}")
            print("Reconnecting in 10 seconds...")
            time.sleep(10)

if __name__ == "__main__":
    try:
        start_bot()
    except KeyboardInterrupt:
        print("\nBot stopped by user.")
    except Exception as e:
        print(f"Fatal error: {e}")
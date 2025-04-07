
import os
import telebot
from flask import Flask, request

API_TOKEN = os.getenv("API_TOKEN")
USER_ID = os.getenv("USER_ID")

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@app.route('/' + API_TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return '!', 200

@app.route("/", methods=['GET', 'POST'])
def webhook():
    return "Bot is running!"

def send_message(text):
    bot.send_message(USER_ID, text)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port)

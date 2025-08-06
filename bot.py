import time
import ccxt
import telebot
from config import API_KEY, API_SECRET, TELEGRAM_TOKEN, CHAT_ID, USE_TESTNET

# Exchange setup
exchange = ccxt.bybit({
    'apiKey': API_KEY,
    'secret': API_SECRET,
})
if USE_TESTNET:
    exchange.set_sandbox_mode(True)

# Telegram bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Example task
def check_balance():
    balance = exchange.fetch_balance()
    return balance['total']

@bot.message_handler(commands=['balance'])
def send_balance(message):
    if str(message.chat.id) == CHAT_ID:
        bal = check_balance()
        bot.reply_to(message, f"Balance: {bal}")

bot.send_message(CHAT_ID, "🤖 Bybit bot started!")
bot.polling()

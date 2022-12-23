import random
import telebot
from telebot import types


randnum = random.randint(1,41)
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('New Game')
markup.add(itembtn1)

bot = telebot.TeleBot("5855476837:AAFic6w9zD1XPESnfDCoUyNQiBo5fdRQHRg", parse_mode=None)
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

  name = message.from_user.first_name
  bot.reply_to(message, f"Welcome {name}!")
  bot.send_message(message.from_user.id,"""Bot Commands:
	/start: for Telling Welcome
	- - - -
	/game: guess number Game
	- - - -
	/age: calculate your age
	- - - -
	/voice: Converts text to voice
	- - - -
	/qrcode: make a QR code from your text
	- - - -
	/max: Find maximum number of the array
	- - - -
	/argmax: Find index of maximum number of the array
	- - - -
	/help: commands list
	""")

@bot.message_handler(commands=['game'])
def game(message):
	global randnum
	bot.reply_to(message,"""Welcome to 'Guess the Number' game.
	you have to guess a number between 1 and 40.""")
	guess = bot.send_message(message.chat.id, "Enter a number between 0 and 40:" , reply_markup=markup)

	
	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
			if message.text == "hi":
				bot.reply_to(message, "Hi!")


bot.infinity_polling()



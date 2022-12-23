import random
import telebot
from telebot import types
from khayyam import JalaliDate, JalaliDatetime 

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('/New_Game')
markup.add(itembtn1)

bot = telebot.TeleBot(<TOKEN>, parse_mode=None)
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

@bot.message_handler(commands=['game','New_Game'])
def game(message):
	global cpu
	cpu = random.randint(1,41)
	bot.reply_to(message,"""Welcome to 'Guess the Number' game.
	you have to guess a number between 1 and 40.""")
	guess1 = bot.send_message(message.chat.id, "Enter a number between 0 and 40:" , reply_markup=markup)
	bot.register_next_step_handler(guess1,guess)

@bot.message_handler(func=lambda m: True)
def guess(message):
	isint = (message.text).isdigit()
	if isint == False:
		m = bot.send_message(message.chat.id,"please enter a number not a string")
	
	elif int(message.text) > cpu:
		m = bot.send_message(message.chat.id,"guess a smaller number⬆")
		bot.register_next_step_handler(m, guess )
	 
	elif int(message.text) < cpu:
		m = bot.send_message(message.chat.id,"guess a bigger number⬇")
		bot.register_next_step_handler(m, guess )
	 
	elif int(message.text) == cpu:
		m = bot.send_message(message.chat.id, "Congratulations🎉, YOU WIN!", reply_markup= telebot.types.ReplyKeyboardRemove(selective=True))
		bot.register_next_step_handler(m, guess )
	
@bot.message_handler(commands= ["age"])
def birth(message):
  date = bot.send_message(message.chat.id, "Enter your date of birth (year/month/day):")
  bot.register_next_step_handler(date, age)

def age(message):
  birthday = str(message.text).split()
  age1 = JalaliDatetime.now() - JalaliDatetime(birthday[0], birthday[1], birthday[2]) // 365
  bot.send_message(message.chat.id,"Your age is: ", age1)
		

bot.infinity_polling()

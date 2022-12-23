import random
import telebot
from telebot import types
from khayyam import JalaliDate, JalaliDatetime 
import gtts
import qrcode

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('/New_Game')
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

@bot.message_handler(commands=['game','New_Game'])
def game(message):
	global cpu
	cpu = random.randint(1,41)
	bot.reply_to(message,"""Welcome to 'Guess the Number' game.
	you have to guess a number between 1 and 40.""")
	guess1 = bot.send_message(message.chat.id, "Enter a number between 0 and 40:" , reply_markup=markup)
	bot.register_next_step_handler(guess1,guess)


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
  birthDate = message.text.split("/")
  difference = JalaliDatetime.now() - JalaliDatetime(birthDate[0], birthDate[1], birthDate[2])
  year = difference.days // 365
  difference = difference.days % 365
  month = difference // 30
  day = difference % 30 - 7
  bot.send_message(message.chat.id, "your age: " + str(year) + " years and " + str(month) + " months and " + str(day) + " days")

@bot.message_handler(commands= ["voice"])
def voice(message):
	msg = bot.send_message(message.chat.id,"Enter a text to convert in voice.")
	bot.register_next_step_handler(msg,convert)
def convert(message):
  sound2 = gtts.gTTS(text = message.text , lang = "en" , slow = False )
  sound2.save("VoiceBot.ogg")
  audio = open("VoiceBot.ogg", 'rb')
  bot.send_audio(message.chat.id, audio)

@bot.message_handler(commands= ["max"])
def input_array(message):
	msg = bot.send_message(message.chat.id,"Please Enter an array to find the max number.(e.g: 2,3,4,1,7,0 = 7)")
	bot.register_next_step_handler(msg,max_array)

def max_array(message):
	text = message.text.split(",")
	max = 0
	for num in text:
		if max < int(num):
			max = int(num)
	bot.send_message(message.chat.id, f"The maximum number of your array is {max}")
 
@bot.message_handler(commands= ["argmax"])
def input_array(message):
	msg = bot.send_message(message.chat.id,"Please Enter an array to find the index of max number.(e.g: 2,3,4,1,7,0 = 4)")
	bot.register_next_step_handler(msg,argmax)

def argmax(message):
	text = message.text.split(",")
	max = 0
	ind = 0
	for num in text:
		if max < int(num):
			max = int(num)
			index = ind
		ind += 1
	bot.send_message(message.chat.id, f"The maximum index number of your array is {index}")
 
@bot.message_handler(commands= ["qrcode"]) 
def input_qr(message):
	data = bot.send_message(message.chat.id,"write a text to convert it to qrcode.")
	bot.register_next_step_handler(data,qr)

def qr(message):
	img = qrcode.make(message.text)
	img.save("qrcode.png")
	img2 = open("qrcode.png","rb")
	bot.send_photo(message.chat.id, img2)
 
bot.infinity_polling()

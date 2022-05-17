import telebot 

import requests

from dateb import *

from telebot import types





API_TOKEN = '5371686399:AAEnXevd0OcJsHeNmB5DFflPQ3K_91jPwv0'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['Start'])
def welcome(message):
		bot.send_message(message.chat.id,'Hello, im bot for your timetable, use "/help" to see my options')

@bot.message_handler(commands = ['Help'])
def help(message):
	bot.send_message(message.chat.id, """Available Commands :-
	/link - To get the Link to a class
	/Info - To get info about your professor
	/Shedule - To get shedule your class
	/Add - Add your info""")


@bot.message_handler(commands = ['link'])
def link(message):
	bot.send_message(message.chat.id,
		"!!!!")

@bot.message_handler(commands = ['Info'])
def info(message):
	bot.send_message(message.chat.id,
		"!!!")


@bot.message_handler(commands = ['Shedule'])
def shedule(message):
	for i in range(len(Shedules)):
		bot.send_message(message.chat.id, ",".join(Shedules[i]))

@bot.message_handler(commands = ['Add'])
def get_message(message):
	
	bot.send_message(message.chat.id,"Enter day:")
	bot.register_next_step_handler(message,get_message)
def get_message(message):
	day = message.text

	bot.send_message(message.chat.id,	
		"""Enter lessons, time, link:
		(Example: Math,15:00,/Link..,Chemistry,16:45,/Link..,...)""")

	bot.register_next_step_handler(message,get_lessons_and_time, day=day)

def get_lessons_and_time(message,day):
	
	user_input = message.text
	user_input = user_input.split(',')

	
	bot.send_message(message.chat.id, f"Your shedule on {day}")
	for i in range(0,len(user_input),3):
		bot.send_message(message.chat.id, f'{user_input[i]} {user_input[i+1]} {user_input[i+2]}')
	input_bd(user_input)

bot.polling()
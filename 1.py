import telebot 

import requests

from telebot import types




API_TOKEN = '5371686399:AAEnXevd0OcJsHeNmB5DFflPQ3K_91jPwv0'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
		bot.send_message(message.chat.id,'Hello, im bot for your timetable, use "/help" to see my options')

@bot.message_handler(commands = ['help'])
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
	bot.send_message(message.chat.id,
		day)



@bot.message_handler(commands = ['Add'])
def get_message(message):
	
	bot.send_message(message.chat.id,"Enter day:")
	bot.register_next_step_handler(message,get_message)
def get_message(message):
	print(1)
	
	day = message.text
		
	print(day)
	bot.send_message(message.chat.id,	
		"Enter lessons and time:\n"
		"(Example: Math,15:00,Chemistry,16:45,...)")

	bot.register_next_step_handler(message,get_lessons_and_time)
def get_lessons_and_time(message):
	dict_lessons = {}
	user_info = message.text
	us_info_split = user_info.split(',')
	bot.send_message(message.chat.id, us_info_split)
	print(us_info_split)

	for i in range(0,len(us_info_split),2):
		dict_lessons[user_info[i]]=user_info[i+1]
	print(dict_lessons)
bot.polling()
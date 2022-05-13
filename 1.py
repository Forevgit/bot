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
	@bot.message_handler(content_types=['text'])
	def get_message(message):
		print(1)

		
		day = message.text

		bot.send_message(message.chat.id,"Enter amount  lessons")
		
		bot.register_next_step_handler(message,amount_lessons_getter)
	
	def amount_lessons_getter(message):
		print(2)
		
		
		amount = int(message.text)

		
		bot.register_next_step_handler(message,timetable_dct,amount)

	@bot.message_handler(content_types=['text'])
	def timetable_dct(message,amount):
		print(3)
		dct_lessons={}

		for i in range(amount):
		
			user_inp = math,16.40,qweqwe,12.50

			user_inp.split(',')
			for i step(2)
				dctp[user_inpp[i]]=user_inp[i+1]


			bot.send_message(message.chat.id,"Enter lessons")
			lesson=message.text
			
			bot.send_message(message.chat.id,"Enter time")
			
			dct_lessons[lesson]=message.text

			

		bot.send_message(message.chat.id, dict)
			



bot.polling()
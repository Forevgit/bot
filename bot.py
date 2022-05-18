import telebot 

import requests

from dateb import *

from telebot import types





API_TOKEN = '5371686399:AAEnXevd0OcJsHeNmB5DFflPQ3K_91jPwv0'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['Start'])
def welcome(message):
		bot.send_message(message.chat.id,'Hello, im bot for your timetable, use "/Help" to see my options')

@bot.message_handler(commands = ['Help'])
def help(message):
	bot.send_message(message.chat.id, """Available Commands :-
	/link - To get the Link to a class
	/Info - To get info about your professor
	/Schedule - To get shedule your class
	/Add - Add your info
	/Delete - Delete all info""")


@bot.message_handler(commands = ['link'])
def link(message):
	links = get_link()
	answer = ""
	for lesson,link in links:
 		answer += f"{lesson}: {link}\n\n\n"
	bot.send_message(message.chat.id,answer)


@bot.message_handler(commands = ['Info'])
def info(message):
	for i in range(len(get_info())):
		bot.send_message(message.chat.id, " викладає: ".join(get_info()[i]))
	


@bot.message_handler(commands = ['Schedule'])
def shedule(message):
	#schedule = get_schedule()
	#answer = schedule(0,2)
	for i in range(len(get_schedule())):
		bot.send_message(message.chat.id, ", ".join(get_schedule()[i]))

@bot.message_handler(commands = ['Delete'])
def shedule(message):
	delete_all()
	bot.send_message(message.chat.id,"Your schedule was delete")

@bot.message_handler(commands = ['Add'])
def get_message(message):
	
	bot.send_message(message.chat.id,"Enter day:")
	bot.register_next_step_handler(message,get_message)
def get_message(message):
	day = message.text

	bot.send_message(message.chat.id,	
		"""Enter lessons, time, link, Professor:
		(Example: Чисельні методи,15:00,/Link..,Світлана Борисівна,ПРП,16:45,/Link..,Леся Ігорівна,...)""")

	bot.register_next_step_handler(message,get_lessons_and_time, day=day)

def get_lessons_and_time(message,day):
	
	user_input = message.text
	user_input = user_input.split(',')

	
	#bot.send_message(message.chat.id, f"Your shedule on {day}")
	#for i in range(0,len(user_input),3):
	#	bot.send_message(message.chat.id, f'{user_input[i]} {user_input[i+1]} {user_input[i+2]}')
	input_bd(day,user_input)


bot.polling()
import telebot 

import requests

from dateb import *

from telebot import types





API_TOKEN = '5371686399:AAEnXevd0OcJsHeNmB5DFflPQ3K_91jPwv0'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['start'])
def welcome(message):
		bot.send_message(message.chat.id,'Привіт, я бот для вашого розкладу предметів/уроків, введіть команду "/help" щоб побачити доступні команди')

@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, """Доступні команди :-
	/link - Отримати посилання на пару
	/Info - Отримати інформацію про викладача і пару яку він проводить
	/Schedule - Отримати ваш розклад 
	/Add - Добавити вашу інформацію
	/Delete - Видалити вашу інформацію""")


@bot.message_handler(commands = ['link'])
def link(message):
	links = get_link()
	answer = ""
	for lesson,link in links:
 		answer += f"{lesson}: {link}\n\n\n"
	bot.send_message(message.chat.id,answer)


@bot.message_handler(commands = ['Info'])
def info(message):
	answer = ""
	infors = get_info()
	for Name_lastname,Lesson in infors:
		answer += f'{Name_lastname}: {Lesson}\n\n'
	bot.send_message(message.chat.id, answer)
	


@bot.message_handler(commands = ['Schedule'])
def shedule(message):
	days = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', 'Пятниця']
	answer = ""
	for day in days:
		answer += day + ':\n'
		schedule = get_schedule(day)
		for lesson,time in schedule:
			answer += f'{lesson}: {time}\n'
		answer += "\n"
	bot.send_message(message.chat.id, answer)

@bot.message_handler(commands = ['Delete'])
def shedule(message):
	delete_all()
	bot.send_message(message.chat.id,"Ваша інформація видалена")

@bot.message_handler(commands = ['Add'])
def get_message(message):
	
	bot.send_message(message.chat.id,"Введіть день:")
	bot.register_next_step_handler(message,get_message)
def get_message(message):
	day = message.text

	bot.send_message(message.chat.id,	
		"""Введіть ваш предмет, час, посилання, викладач:
		(Приклад: Чисельні методи, 15:00, /Link.., Світлана Борисівна, ПРП, 16:45, /Link.., Леся Ігорівна,...)""")

	bot.register_next_step_handler(message,get_lessons_and_time, day=day)

def get_lessons_and_time(message,day):
	
	user_input = message.text
	user_input = user_input.split(', ')
	input_bd(day,user_input)


bot.polling()
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




#@bot.message_handler(commands = ['add'])
#def add(message):
#	bot.send_message(message.chat.id,
#		"!!!")


#@bot.message_handler(commands = ['add'])
# def bot.send_messasge("input time , subject (TO STOP TYPE "STOP")")
#
#
#   if(bot.message.Text()=="stop")
#     break
#
#
#  lst=bot.message.Text()
#
day = ''
time = 0
subject = ''
message= ''
lst=('asd')
#@bot.message_handler(commands = ['Add'])
#def get_message(str: message):
#	bot.send_message(message.chat.id, 
#		 "day, time, subject")
#	lst = message.text(message)

@bot.message_handler(commands = ['Shedule'])
def shedule(message):
	bot.send_message(message.chat.id,
		day)


@bot.message_handler(commands = ['Text'])
def get_message(message):
	global day
	day = bot.message.Text





bot.polling()
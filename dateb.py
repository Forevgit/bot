import pymysql
from config import host, user, password, db_name
import datetime




try:
	connection = pymysql.connect(
	host = "localhost",
  	port = 3306,
 	user = "root",
  	password = "Nikewasd2015",
  	database = "test",
	)

	print("Successfully connected")
	def create_db():
		with connection.cursor() as cursor:
			create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT,Day varchar(32),Lesson varchar(64), Name_lastname varchar(64),Link varchar(256),Time Time, PRIMARY KEY (id))"
			cursor.execute(create_table_query)
			print("Table created successfully")

	def get_info():
		Infors = list()
		with connection.cursor() as cursor:
			cursor.execute("SELECT distinct Name_lastname, Lesson FROM `users`;")
			rows = cursor.fetchall()
			for row in rows:
				Infors.append(row)
		return Infors

	def get_link():	
		Links = list()	
		with connection.cursor() as cursor:
			cursor.execute("SELECT distinct Lesson, Link FROM `users`;")
			rows = cursor.fetchall()
			for row in rows:
				Links.append(row)
		return Links
	def get_schedule():	
		Shedules = list()	
		with connection.cursor() as cursor:
			cursor.execute("SELECT Lesson, Time, Day FROM `users`;")
			rows = cursor.fetchall()

			for row in rows:
				row = list(row)
				row[1]=str((datetime.datetime.min + row[1]).time())[:-3]
				Shedules.append(row)
		return Shedules
except Exception as ex:
	print("Connection refused")
	print(ex)

def input_bd(day,user_input):
	with connection.cursor() as cursor:
		for i in range(0, len(user_input),4):
			insert_query = f"INSERT INTO `users`(`Day`,`Lesson`, `Time`, `Link`, `Name_lastname`) VALUES ('{day}', '{user_input[i]}', '{user_input[i+1]}', '{user_input[i+2]}', '{user_input[i+3]}')"
			cursor.execute(insert_query)
	connection.commit()


def delete_all():
	with connection.cursor() as cursor:
		delete_all = "DELETE FROM `users`;"
		cursor.execute(delete_all)
	connection.commit()
import pymysql
from config import host, user, password, db_name
import datetime

Links = list()
Infors = list()
Shedules = list()
try:
	connection = pymysql.connect(
	host = "localhost",
  	port = 3306,
 	user = "root",
  	password = "Nikewasd2015",
  	database = "test",
	)

	print("Successfully connected")

#	with connection.cursor() as cursor:
#		insert_query = "INSERT INTO `tt`(`id`, `Name`, `Time`, `Link`, `Day`) VALUES ('2','Max','11:21','dldldd','Tuesday')"
#		cursor.execute(insert_query)
#		connection.commit()
	#with connection.cursor() as cursor:
	#	create_table_query = "CREATE TABLE `users`(id int AUTO_INCREMENT,Link varchar(32),Time Time,Day varchar(32), PRIMARY KEY (id))"
	#	cursor.execute(create_table_query)
	#	print("Table created successfully")
	with connection.cursor() as cursor:
		cursor.execute("SELECT Day FROM `tt`;")
		rows = cursor.fetchall()
		for row in rows:
			Links.append(row)
	with connection.cursor() as cursor:
		cursor.execute("SELECT Link FROM `tt`;")
		rows = cursor.fetchall()
		for row in rows:
			Infors.append(row)
	with connection.cursor() as cursor:
		cursor.execute("SELECT Day, Time, Link FROM `users`;")
		rows = cursor.fetchall()

		for row in rows:
			row = list(row)
			row[1]=str((datetime.datetime.min + row[1]).time())[:-3]
			Shedules.append(row)
		print(Shedules)
	

except Exception as ex:
	print("Connection refused")
	print(ex)

def input_bd(user_input):
	with connection.cursor() as cursor:
		for i in range(0, len(user_input),3):
			insert_query = f"INSERT INTO `users`(`Day`, `Time`, `Link`) VALUES ('{user_input[i]}', '{user_input[i+1]}', '{user_input[i+2]}')"
			cursor.execute(insert_query)
			print(insert_query)
	connection.commit()
import pymysql
from config import host, user, password, db_name

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

	try:
	#	with connection.cursor() as cursor:
	#		insert_query = "INSERT INTO `tt`(`id`, `Name`, `Time`, `Link`, `Day`) VALUES ('2','Max','11:21','dldldd','Tuesday')"
	#		cursor.execute(insert_query)
	#		connection.commit()

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
			cursor.execute("SELECT id FROM `tt`;")
			rows = cursor.fetchall()
			for row in rows:
				Shedules.append(row)
	finally:
		connection.close()
except Exception as ex:
	print("Connection refused")
	print(ex)



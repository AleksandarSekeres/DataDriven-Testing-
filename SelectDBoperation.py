import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
	curs=con.cursor()	
	curs.execute("select * from student")
	for row in curs:
		print(row[0],row[1],row[2])	#for loop for printing data from the table
	con.close()
except:
	print("connection unsuccesfull...")
print("Finished")
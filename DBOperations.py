# insert, update, delete

#	import mysql.connector

#	con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
#	curs=con.cursor()	#create cursor
#	curs.execute("insert into student values(104,'KimZ')")	#execute query through cursor
#	con.commit()	#commit transaction
#	con.close()

#	print("finished")



insert_query="insert into student values(104,'KimZ')"
update_query="update student set sname='abc' where sid=103"
delete_query="delete from student where sid=103"
import mysql.connector

con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
curs=con.cursor()	#create cursor
curs.execute(insert_query)	#insted of writing whole statement
con.commit()	#commit transaction
con.close()

print("finished")

#handling exceptions

insert_query="insert into student values(104,'KimZ')"
update_query="update student set sname='abc' where sid=103"
delete_query="delete from student where sid=103"
import mysql.connector
try:
	con=mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
	curs=con.cursor()	
	curs.execute(insert_query)	
	con.commit()	
	con.close()
except:
	print("connection unsuccesfull...")
print("Finished")
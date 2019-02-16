import os
import sqlite3
from docx import Document
from docx.shared import Inches
def data_base_read():
	conn = sqlite3.connect('Chinook_Sqlite.sqlite')
	cursor = conn.cursor()
	#conn = psycopg2.connect( host=hostname, user=username, password=password, dbname=database)
	cursor.execute("SELECT Name FROM Artist ORDER BY Name LIMIT 3")


	results = cursor.fetchall()
	results2 =  cursor.fetchall()

	print(results)   
	print(results2)  
	conn.close()
	return main()
def write_docs():
	return main()
def main():
	print ('1.')
	print('2.')
	print('3.')
	choose = input ()
	if choose == '1':
		return data_base_read()
if __name__ == '__main__':
	main()
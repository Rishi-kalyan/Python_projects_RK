import cx_Oracle
dsn = cx_Oracle.makedsn('localhost', 1521, 'xe')
connection = cx_Oracle.connect('hr', 'hr', dsn)
cursor = connection.cursor()
cursor.execute('SELECT * FROM employees')
results = cursor.fetchall()
print(results)
connection.close()
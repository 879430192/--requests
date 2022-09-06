import mysql.connector
cx = mysql.connector.connect(user = 'root',password = '123456',host='localhost',database = 'qw')
print(cx)
cx.close()
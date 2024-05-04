import mysql.connector

conexion = mysql.connector.connect(
    user = '',
    password = '',
    host = 'localhost',
    database = 'test', port = '3306')

# print(conexion)

cursor = conexion.cursor()

# Mostrar las bases de datos existentes

# cursor.execute("SHOW DATABASES")

"""
for bd in cursor:
    print(bd)
"""

cursor.execute("SELECT * FROM users")

tupla = cursor.fetchall()

# print(tupla)

for fila in tupla:
    print(fila)

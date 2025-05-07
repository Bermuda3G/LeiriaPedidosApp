import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Barb@rvore54'
)

#Preparando um cursor object
cursorObject = dataBase.cursor()

#Criando a database
cursorObject.execute("CREATE DATABASE leiriaBD")

print("leiriaBD criado com sucesso")
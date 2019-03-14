# Created by AMINE AWAD ABED on 07/10/18.
# Copyright © 2018 AMINE AWAD ABED. All rights reserved.
# muestra el número de bases de datos que se tienen
 
# crea la base datos '2grado' en dbMaria o MySql (funciona para las 2 es lo mismo)
# crea la tablas de datos
# versión del 03 de marzo 2019 01:30 pm
 
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='polifemus')
a=conn.cursor()
sql='show databases';
sql2='create database 2grado'
a.execute(sql)
a.execute(sql2)
alfa=a.execute(sql)
print('Tienes:',alfa,'Bases de datos')
sql3='use 2grado;'
sql4='create table datos (numero int auto_increment,a float(8,2),b float(8,2),c float(8,2),r1 float(8,2),r2 float(8,2),tipo varchar(30),primary key (número));'
a.execute(sql3)
a.execute(sql4)



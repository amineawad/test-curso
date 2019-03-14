#    Created by AMINE AWAD ABED on 04/09/18.
#    Copyright © 2018 AMINE AWAD ABED. All rights reserved.
#    versión noviembre 25 2018 10:46 (incluye gráficas y almacenar los resultados en dbMaria y SqlLite)
#    versión dual 11 de MARZO 2019 (se almacena de MySql y SqlLite) al mismo tiepo
# Ecuación de Segundo Grado
# Ax²+Bx+C
import sys
import math  # para operar la raíz cuadrada
import cmath  # para operaciones con números complejos
print("Ingrese los coeficientes de la ecuación:")
print("         Ax²+Bx+C=0")
print(" ")
a = float(input('Introduce el valor de A= '))
b = float(input('Introduce el valor de B= '))
c = float(input('Introduce el valor de C= '))
discr = (b ** 2 - 4 * a * c)  # discriminante
den = 2 * a
term = math.sqrt(abs(discr))
if discr >= 0:
   x1 = (-b + term) / den
   x2 = (-b - term) / den
   print(" ")
   print("La solución para la ecuación:")
   print (a, 'x²', b, 'x', c)
   print(" ")
   print("La solución tiene 2 raíces reales")
   print(" ")
   print("Raíz 1=", x1)
   print("Raíz 2=", x2)
   print(" ")
   titulo1 = ('Gráfica de la Ecuación: ', a, 'x²', b, 'x', c)
   titulo2 = (a, 'x²', b, 'x', c)
   print(" ")
   #  Gráfica de la Ecuación para soluciones reales
   print(" ")
   print(" ")
   print("SE REQUIERE INGRESAR EL RANGO DEL EJE-X ")
   print("Por Ejemplo 20 , esto quiere decir que el EJE_X va de -20 @ 20")
   print(" ")
   print("El rango tiene que abarcar los valores de:",round(x1,2),"y",round(x2,2))
   print(" ")
   int1 = float(input('Introduce el rango de la gráfica '))


   from matplotlib import pyplot
   import matplotlib.pyplot as plt
   import numpy as np

   pyplot.axhline(0, color="red")
   pyplot.axvline(0, color="red")
   x = np.arange(-int1, int1, .001) #(int1,int2,incre)
   # int1,int2 son los intervalos
   # incre es el incremento
   y = a * x ** 2 + b * x + c  # gráfica
   plt.grid(True)
   plt.plot(x, y, label=titulo2)
   plt.title(titulo1, fontsize=12)
   plt.xlabel('EJE-X', fontsize=10)
   plt.ylabel('EJE-Y', fontsize=10)
   plt.legend()
   p1 = round(x1, 3)
   p2 = round(x2, 3)

   # Anotaciones y Flecha sobre la Gráfica
   # raíz-1
   plt.annotate(p1, xy=(p1, 0), xytext=(p1, 2.5), arrowprops=dict(facecolor='yellow', shrink=0), )

   # raíz-2
   plt.annotate(p2, xy=(p2, 0), xytext=(p2, 2.5), arrowprops=dict(facecolor='magenta', shrink=0), )

   # imagenes (diferentes formatos)
   plt.savefig('ec2grado.png') # Portable Network Graphics
#  plt.savefig('ec2grado.pdf') # Portable Document Format
#  plt.savefig('ec2grado.svg') # Scalable Vector Graphics
#  imagenes
   plt.show()
   print(" ")
   print("La solución son 2 raíces reales")
   print(" ")
   print("Raíz 1=", x1)
   print("Raíz 2=", x2)
   
 #acceso a la base de datos 2grado
   import pymysql
   conn=pymysql.connect(host='localhost',user='root',password='polifemus',db='2grado')
   x=conn.cursor()
   x.execute("""INSERT INTO datos VALUES (null,%s,%s,%s,%s,%s,%s)""",(a,b,c,x1,x2,'Real'))
   # el campo null es para el id que es auto_increment
   conn.commit()
   conn.rollback()
   conn.close()
   print(" ")
   print ("Datos almacenados en la base de datos 2grado de MySql")
   import sqlite3
   miconexion=sqlite3.connect("2grado.db")
   micursor=miconexion.cursor()
   v1=a
   v2=b
   v3=c
   v4=x1
   v5=x2
   v6='Real'
   micursor.execute("INSERT INTO datos VALUES (null,?,?,?,?,?,?)",(v1,v2,v3,v4,v5,v6))
   miconexion.commit()
   miconexion.close()
   print(" ")
   print("Datos almacenados en la base de datos 2g_sqlite.db sw SQlLite")
   
   sys.exit()  # se interrupe el programa
else:
   x1 = -b / den
   x2 = term / den
   print(" ")
   print("La solucón es imaginaría (par conjugado)")
   print(" ")
   print("para la ecuacion: ",a, 'x²', b, 'x', c)
   print(" ")
   print('x1=', x1, '+', x2, 'i')
   print('x2=', x1, '-', x2, 'i')
   print(" ")
   c1 = complex(x1, x2)  # convertimos c1 a número complejo
   print('SOLUCIÓN PAR CONJUGADO:= ', c1)
   polar = cmath.polar(complex(x1, x2))
   phase = cmath.phase(complex(x1, x2))
   modulo = abs(complex(x1, x2))
   print("(resultado con la libreria cmath)")
   print("===================Resultados:===================================")
   print(" ")
   print('El módulo @ Fase=', polar)
   print('La fase es =', phase)
   print('El Módulo es= ', modulo)

   # Gráfica Plano de Argnad números complejos
   # definimos funsión
   import matplotlib.pyplot as plt
def move_spines():
   fix, ax = plt.subplots()
   for spine in ["left", "bottom"]:
       ax.spines[spine].set_position("zero")
   for spine in ["right", "top"]:
       ax.spines[spine].set_color("none")
   return ax
print(" ")  # formateo de las coordenadas de la gráfica

ax = move_spines()
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
ax.grid()
ax.scatter(c1.real, c1.imag)
bb = (c1.imag) * -1
ax.scatter(c1.real, bb)
plt.title("Plano Complejo de Argand", fontsize=11)
plt.savefig('ec2g-plano-Argnad.png')
p1 = round((c1.real), 3)
p2 = round((c1.imag), 3)

#plt.annotate(p1, xy=(p1, bb), xytext=(p1, bb), arrowprops=dict(facecolor='blue', shrink=0), )
#plt.annotate(p2, xy=(-p2, 4), xytext=(-p2, 4), arrowprops=dict(facecolor='red', shrink=0), )
plt.show()

# se alamcena en la base de datos '2grado_b' los resultados
import pymysql
conn=pymysql.connect(host='localhost',user='root',password='polifemus',db='2grado')
x=conn.cursor()
x.execute("""INSERT INTO datos VALUES (null,%s,%s,%s,%s,%s,%s)""",(a,b,c,x1,x2,'Imaginaría par conjugado'))
# el campo null es para el id que es auto_increment
conn.commit()
conn.rollback()
conn.close()
print ("Datos almacenados en la base de datos 2grado de MySql")
import sqlite3
miconexion=sqlite3.connect("2grado.db")
micursor=miconexion.cursor()
v1=a
v2=b
v3=c
v4=x1
v5=x2
v6='Imaginaría par conjugado'
micursor.execute("INSERT INTO datos VALUES (null,?,?,?,?,?,?)",(v1,v2,v3,v4,v5,v6))
miconexion.commit()
miconexion.close()
print("Datos almacenados en la base de datos 2grado.db de SQlLite")





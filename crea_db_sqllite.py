#    Created by AMINE AWAD ABED on 04/09/18.
#    Copyright © 2018 AMINE AWAD ABED. All rights reserved.
#    versión marzo 5 2019

# programa para crear la base de datos y la tabla datos


import sqlite3
conn=sqlite3.connect('2grado.db')
c=conn.cursor()
c.execute("""CREATE TABLE datos (
              id integer primary key autoincrement,
              a real,
              b real,
             c real,
            r1 real,
            r2 real,
           tipo text
                       ) """)


conn.commit()
conn.close()


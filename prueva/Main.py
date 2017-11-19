'''
Created on 4 sept. 2017

@author: diegoj
'''
from prueva.Mysql import Mysql
from prueva.Sqlite3 import Sqlite
from prueva.PostgreSQL import Post
import sys
'''Clase principal desde la que se ejecutara el blog de notas'''
def main():
    MYSQL = 0
    SQLITE = 1
    POST = 2
    QUIT = 3
    while True:
        print("""
                    Menu Cuaderno
            -------------------------------
            0 Msql
            1 Sqlite3
            2 SQLITE
            3 Salir
            """)
        # Determinar el motor seleccionado
        database_engine = input("Escribe una opcion: ")
        #database_engine =2
        #!/usr/bin/python
        if database_engine == MYSQL:
            mysql = Mysql()
            mysql.run()
        elif database_engine == SQLITE:
            sqlite=Sqlite()
            sqlite.run()
            
        elif database_engine == POST:
            post= Post()
            post.run()
        elif database_engine == QUIT:
            print("Gracias por usar Python")
            sys.exit(0)
        else:
            print("No se ha encontrado %s." % str(database_engine))
    

    
if __name__ == '__main__':
    main()
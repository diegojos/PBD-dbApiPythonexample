'''
Created on 15 nov. 2017

@author: diegoj
'''
import MySQLdb

class Mysql:

    
    def __init__(self):
        print """
                        MySQLdb
                ---------------------
                """
        self.db = MySQLdb.connect("localhost","user","12345","mydb" )
        self.cursor = self.db.cursor()
        self.eleciones ={
            1: self.createtablet,
            2: self.insertejmp,
            3: self.select,
            4: self.update,
            5: self.delete,
            6: self.test,
            7: self.quit
            }
        
    # prepare a cursor object using cursor() method
    def mostrar_menu(self):
        print("""
                Menu MySQL
        -------------------------------
        1 Crear Tabla
        2 Insertar
        3 Visualizar
        4 Actualizar
        5 Borrar
        6 Prueba
        7 Salir
        """)
    def run(self):
        opcion=True
        while opcion:
            self.mostrar_menu()
            eleccion = input("Escribe una opcion:")
            print eleccion
            accion = self.eleciones.get(eleccion)
            if accion:
                if eleccion==7:
                    opcion=accion()
                else:
                    accion()
            else:
                print("{0} no es una eleccion valida".format(eleccion))
 
    def createtablet(self):
        self.cursor.execute("DROP TABLE IF EXISTS Alumnos")
        sql = """CREATE TABLE Alumnos (
        Nombre  CHAR(20) NOT NULL,
        Apellido1 CHAR(20),
        Apellido2 CHAR(20),
        Sex CHAR(1),
        Email CHAR(40))"""
        self.cursor.execute(sql)
    def insertejmp(self):
        print ("""
            
                       Insertando  alumnos 
                  -------------------------------------- 
                   """)
        self.sql = """INSERT INTO Alumnos(Nombre,
        Apellido1, Apellido2, Sex,  Email)
        VALUES ('Diego Jose', 'Merino','Fernandez','M', 'dmerinof@alumno.unex.es')"""
        try:
            self.cursor.execute( self.sql)
            sql = "INSERT INTO Alumnos( Nombre ,\
            Apellido1, Apellido2, Sex, Email)\
            VALUES ('%s', '%s', '%s', '%c', '%s' )" % \
            ('Antonio', 'Narvaez','Lopez','M', 'antonio.narvaez.lopez@gmail.com')
            self.cursor.execute(sql)
  
            self.db.commit()
        except:
            self.db.rollback()
    def select(self):
        self.sql = "SELECT * FROM Alumnos"
        try:
            self.cursor.execute(self.sql)
         
            results = self.cursor.fetchall()
            for row in results:
                name = row[0]
                ape = row[1]
                ape2 = row[2]
                sex = row[3]
                email= row[4]
      
                print "Nombre=%s \n  apellidos= %s %s \n  sex= %s \n  email= %s" % \
                (name, ape, ape2, sex, email )
        except:
            print "Error: unable to fecth data"
            
    def update(self):
        sql = "UPDATE Alumnos SET Email = 'anarvaezn@alumnos.unex.es' WHERE Nombre = '%s'" % ('Antonio')
        try:
            print ("""
            
                   Actualizando email de alumno Antonio
                  -------------------------------------- 
                   """)
               
            self.cursor.execute(sql)
        
            self.db.commit()
            
        except:
            self.db.rollback()
            
    def delete(self):
        sql = "DELETE FROM Alumnos WHERE Nombre = '%s'" % ('Diego Jose')
        print ("""
                        Borrando alumno Diego
                  -------------------------------------- 
                   """)
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
    def quit(self):
        self.db.close()
        print("Gracias por usar MySQL")
        return False
        

    def test(self):
        self.createtablet()
        self.insertejmp()
        self.select()
        self.update()
        self.select()
        self.delete()
        self.select()
            
     


from getpass import getpass
from mysql.connector import connect, Error


class DataBase:

    def __init__(self):
        try:
            aux = connect(
                host ='localhost',
                user ='root',
                password =  'abc.123', # getpass("Antes de continuar, debe que ingresar la clave de administrador de este sistema: \n-------->"),
                database ='cafeteria'
            )
            self.connection = aux
            
        except Error as e:
            print("Error" + e)

    def insert(self,sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            self.close()
        except Error as e:
            print(e)
    def close(self):
        self.connection.close()
        print("Se ha realizado la siguiente accion: ")

    def select(self, tabla,col1,col2,col3,col4,col5,col6,col7):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {tabla};")
        print(f"{col1}  {col2}  {col3}  {col4}  {col5}  {col6}  {col7}")
        for row in cursor.fetchall():
            print(row)
        self.close()

    def select_one(self, tabla, columna, id,col1,col2,col3,col4,col5,col6,col7):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {tabla} WHERE {columna} = {id} ;")
        print(f"{col1}  {col2}  {col3}  {col4}  {col5}  {col6}  {col7}")
        seleccion=cursor.fetchall()
        print(seleccion)
        self.close()
    
    def select_one_bol(self, tabla, columna, ven_cod,col1,col2,col3,col4,col5,col6,col7):
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM {tabla} WHERE {columna} = {ven_cod} ;")
        print(f"{col1}  {col2}  {col3}  {col4}  {col5}  {col6}  {col7}")
        seleccion=cursor.fetchone()
        print(seleccion)
        self.close()

    def select_bol(self, sql, col1,col2,col3,col4,col5,col6,col7):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        print(f"{col1}  {col2}  {col3}  {col4}  {col5}  {col6}  {col7}")
        for row in cursor.fetchall():
            print(row)
        self.close()

    def update(self, sql):

        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        self.close()
    
    def delete(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()
        self.close()
             

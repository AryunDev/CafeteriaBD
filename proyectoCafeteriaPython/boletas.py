from conector import DataBase
class Boletas:

    def __init__(self, iva, total,ven_cod):
        self.iva = iva
        self.total = total
        self.ven_cod = ven_cod

    def insert_bol(self):
        sql = f"INSERT INTO boletas (bol_iva, bol_total, ven_cod) VALUE ({self.iva}, {self.total}, {self.ven_cod});"
        db = DataBase()
        db.insert(sql)

    def mostrar_bol():
        tabla = 'boletas' 
        col1 = "ID"
        col2 = "IVA"
        col3 = "TOTAL"
        col4 = "Código Venta"
        col5 = " "
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select(tabla,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_bol_uq(ven_cod):
        tabla = 'boletas'
        columna = 'ven_cod' 
        col1 = "ID"
        col2 = "IVA"
        col3 = "TOTAL"
        col4 = "Código Venta"
        col5 = " "
        col6 = " "
        col7 = " "
        db = DataBase()
        db.select_one_bol(tabla,columna, ven_cod,col1,col2,col3,col4,col5,col6,col7)

    def mostrar_bol_usu(id):
        sql = f"SELECT u.usu_nom,b.bol_cod, b.bol_iva, b.bol_total, v.ven_descrip, v.ven_cod FROM boletas b JOIN ventas v ON (b.ven_cod = v.ven_cod) JOIN usuarios u ON (v.usu_cod = u.usu_cod) WHERE u.usu_cod = {id};"
        col1 = "USERNAME"
        col2 = "ID"
        col3 = "IVA"
        col4 = "TOTAL"
        col5 = "Descripción "
        col6 = "Código Venta"
        col7 = " "
        db = DataBase()
        db.select_bol(sql, col1,col2,col3,col4,col5,col6,col7)

    def mostrar_bol_cli(id):
        sql = f"SELECT CONCAT(p.per_nombre, p.per_app), b.bol_cod, b.bol_iva, b.bol_total, v.ven_descrip, v.ven_cod FROM boletas b JOIN ventas v ON (b.ven_cod = v.ven_cod) JOIN clientes c ON (v.cli_cod = c.cli_cod) JOIN personas p ON (c.per_run = p.per_run) WHERE c.cli_cod = {id};"
        col1 = "Nombre y Apellido"
        col2 = "Código Boleta"
        col3 = "IVA"
        col4 = "Total"
        col5 = "Descripción"
        col6 = "Código Venta"
        col7 = " "
        db = DataBase()
        db.select_bol(sql, col1,col2,col3,col4,col5,col6,col7)

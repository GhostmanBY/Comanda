import sqlite3

con=sqlite3.connect("menu.db")
cur=con.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS comensales(
        cantidad INTERGER)"""
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS menu(
        nombre TEXT,
        precio REAL
    )
    """
)

cur.execute(
    """CREATE TABLE IF NOT EXISTS pedidos(
        nombre TEXT,
        mesa INTERGER,
        cantidad INTERGER
        )"""
)

con.commit()
con.close()


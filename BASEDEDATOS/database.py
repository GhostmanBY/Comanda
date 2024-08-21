import sqlite3

con=sqlite3.connect("menu_adm.db")
cur=con.cursor()


cur.execute(
    """CREATE TABLE IF NOT EXISTS menu(
        nombre TEXT,
        precio REAL,
        cantidad INTERGER,
        mesa INTERGER
    )
    """
)



con.commit()
con.close()

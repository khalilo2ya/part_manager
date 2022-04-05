import sqlite3

class Database:
    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS parts(id INTEGER PRIMARY KEY, part text, customer text, retailer text, price text)")
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SElECT * FROM parts")
        rows=self.cur.fetchall()
        return rows
    def insert(self, part, customer, retailer, price):
        self.cur.execute("INSERT INTO parts VALUES (NULL, ?,?,?,?)", (part, customer, retailer, price))
        self.conn.commit()
    def remove(self, id):
        self.cur.execute("DELETE FROM parts WHERE id=?",(id,))
        self.conn.commit()
    def update(self, id, part, customer, retailer, price):
        self.cur.execute("UPDATE parts SET part=?, customer=?, retailer=?, price=? WHERE id=?",(part, customer, retailer, price, id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()

db=Database('store.db')        
# db.insert("4GB DDR4 Ram","John Doe", "Microcenter","160")
# db.insert("2GB DDR4 Ram","John Doe", "Microcenter","120")
# db.insert("8GB DDR4 Ram","John Doe", "Microcenter","200")
# db.insert("Nvidia RTX 2080","John Doe", "Microcenter","679")
# db.insert("600w Corsair PSU","John Doe", "Microcenter","130")


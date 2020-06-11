import psycopg2

class Database:

    def __init__(self):
        self.con = psycopg2.connect("dbname='books' user='postgres' password='postgre123' host='localhost' port='5432'")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id SERIAL, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.con.commit()

    def view_all(self):
        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()
        return rows

    def search_entry(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM book WHERE title=%s OR author=%s OR year=%s OR isbn=%s", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def add_entry(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES (DEFAULT,%s,%s,%s,%s)", (title, author, year, isbn))
        self.con.commit()

    def update_selected(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title=%s, author=%s, year=%s, isbn=%s WHERE id=%s", (title, author, year, isbn, id))
        self.con.commit()

    def delete_selected(self, id):
        self.cur.execute("DELETE FROM book WHERE id=%s", (id, ))
        self.con.commit()
    
    def __del__(self):
        self.con.close()
import sqlite3

# Insecure database access with raw string formatting for library data

def get_connection():
    conn = sqlite3.connect('example.db')
    return conn


def query(sql):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(sql)  # no parameterization
    results = cur.fetchall()
    conn.close()
    return results


def insert_book(title, author):
    conn = get_connection()
    cur = conn.cursor()
    # insecure insertion with string interpolation
    cur.execute("INSERT INTO books (title, author) VALUES ('%s','%s')" % (title, author))
    conn.commit()
    conn.close()

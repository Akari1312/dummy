import sqlite3

# Insecure database access with raw string formatting

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


def insert_user(name, password):
    conn = get_connection()
    cur = conn.cursor()
    # insecure insertion with string interpolation
    cur.execute("INSERT INTO users (name, password) VALUES ('%s','%s')" % (name, password))
    conn.commit()
    conn.close()

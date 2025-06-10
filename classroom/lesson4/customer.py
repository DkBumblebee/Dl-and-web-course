import sqlite3


def main():
    #search()
    #delete_row()
    show_all()

def create_table():
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS customers (
            first_name text, 
            last_name text, 
            email text,
            username text,
            password text
        )""")

    conn.commit()
    conn.close()

def add_customer(fn, ln, e, un, pw):
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    c.execute("INSERT INTO customers VALUES(?,?,?,?,?)",(fn, ln, e, un, pw) )
    conn.commit()
    conn.close()
    return True

def show_all():
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    c.execute("SELECT rowid, * FROM customers")

    items = c.fetchall()
    for item in items:
        print(item)
    conn.commit()
    conn.close()

def update_user(id = '1'):
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    query = "Update customers SET first_name = 'Mary' WHERE rowid = ? "
    c.execute(query, id)
    conn.commit()
    conn.close()


def search(name= 'j%'):
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()

    query ="SELECT * FROM customers WHERE first_name like (?)"
    c.execute(query, (name,))
    person = c.fetchall()
    for i in person:
        print(i)


def delete_row():
    conn = sqlite3.connect('customer.db')

    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = 2")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()


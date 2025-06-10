from flask import Flask, render_template, request, redirect
from customer import create_table, show_all, add_customer, update_user
import sqlite3


app = Flask(__name__)
create_table()



@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        first_name = request.form["name"]
        last_name = request.form["surname"]
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]

        
        capture = add_customer(first_name, last_name, email, username, password)

        if capture:
            update_user()
            show_all()
            return "Successs"
        return "Fail"
    return "Cannot connect"
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector

app = Flask(__name__)
mysql = MySQLConnector(app,'friends_ex')

@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    for user in users:
        print user['first_name']

    return render_template('index.html', all_users = users)

@app.route('/add', methods=['POST'])
def add():
    query = ("INSERT INTO users (first_name, last_name, age, created_at) VALUES (:first_name, :last_name, :age, NOW())")

    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "age" : request.form['age']
    }

    mysql.query_db(query, data)
    return redirect('/')

app.run(debug = True)

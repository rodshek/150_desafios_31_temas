import sqlite3

from flask import Flask, jsonify, request

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()


@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    conn.close()
    return jsonify({'users': users})


@app.route('/user', methods=['POST'])
def add_user():
    data = request.json
    name = data.get('name')
    age = data.get('age')
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User added successfully'})


if __name__ == '__main__':
    init_db()
    app.run(debug=True)

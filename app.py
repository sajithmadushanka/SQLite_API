import sqlite3
from flask import Flask, request, jsonify,json

app = Flask(__name__)
def get_db_connection():
    conn = sqlite3.connect('books.sqlite')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/get_users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    if request.method == 'GET':
        users = conn.execute('SELECT * FROM user').fetchall()
        users = [dict(row) for row in users]
        return jsonify(users)
    

@app.route('/get_user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM user WHERE id = ?',
                        (user_id,)).fetchone()
    if user:
        return jsonify(dict(user))
    else:
        return "Not found", 404

@app.route('/create_user', methods=['POST'])
def create_user():
    conn = get_db_connection()
    new_user = request.get_json()
    conn.execute('INSERT INTO user (name, age) VALUES (?, ?)',
                 (new_user['name'], new_user['age']))
    conn.commit()
    return "OK", 201

@app.route('/update_user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    conn = get_db_connection()
    user = request.get_json()
    conn.execute('UPDATE user SET name = ?, age = ? WHERE id = ?',
                 (user['name'], user['age'], user_id))
    conn.commit()
    return "OK", 200

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM user WHERE id = ?', (user_id,))
    conn.commit()
    return "OK", 200


if __name__ == '__main__':
    app.run(debug=True)
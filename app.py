from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM products"
    if request.method == 'POST':
        search_term = request.form['search_term']
        query = "SELECT * FROM products WHERE name LIKE ?"
        cursor.execute(query, ('%'+search_term+'%',))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

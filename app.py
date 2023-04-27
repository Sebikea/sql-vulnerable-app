from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("query")
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products WHERE name = '{}'".format(query))
    results = cursor.fetchall()
    return render_template("results.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)


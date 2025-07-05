from flask import Flask, request, jsonify, render_template
import mysql.connector
from flask_cors import CORS
from datetime import date

app = Flask(__name__)
CORS(app)

# ✅ MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1125",
    database="worlddb"
)

# ✅ Route 1: Main Clock Page
@app.route('/')
def index():
    return render_template("index.html", today=date.today())

# ✅ Route 2: Countdown Page
@app.route('/countdown')
def countdown():
    return render_template("countdown.html", today=date.today())

# ✅ Route 3: World Page
@app.route('/world')
def world():
    return render_template("world.html", today=date.today())
@app.route('/timer')
def timer():
    return render_template("timertab.html")

@app.route('/setting')
def setting():
    return render_template("setting.html")


# ✅ Route 4: Country Search
@app.route('/country/<name>')
def get_country(name):
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM countries WHERE name = %s"
    cursor.execute(query, (name,))
    country = cursor.fetchone()
    cursor.close()

    if country:
        return jsonify(country)
    else:
        return jsonify({"error": "Country not found"}), 404

# ✅ Run the app
if __name__ == '__main__':
    app.run(debug=True)

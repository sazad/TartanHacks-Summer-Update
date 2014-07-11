import os
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'textbooks.db'),
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row 
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

@app.route("/")
def beginning():
	return render_template('opening.html')

@app.route("/seller.html")
def hello():
    return render_template("seller.html")

@app.route("/saleposted.html", methods=["POST"])
def addTextbook():
    cNum = request.form['courseNum']
    email = request.form['email']
    name = request.form['textName']
    price = request.form['price']
    addToDatabase(price, cNum, email, name)
    return render_template('saleposted.html')

def addToDatabase(price, cNum, email, name):
    cur = get_db()
    cur.execute("INSERT INTO forsale (courseNum, email, name, price) VALUES (?,?,?,?)", cNum, email, name, price)
    cur.commit()
    return redirect(url_for('beginning'))

@app.route("/buyer.html")
def allTextbooks():
	return render_template('buyer.html')

@app.route("/textbooks.html", methods=["POST"])
def searchTextbooks():
    return render_template('textbooks.html')

if __name__ == "__main__":
	app.run(debug=True)


from flask import Flask, request, render_template
import pymysql
app = Flask(__name__)

db = pymysql.connect(host="localhost", user="root", passwd="root", db="textbooks")

cur = db.cursor() 

@app.route("/")
def beginning():
	return render_template('opening.html')

@app.route("/seller.html")
def hello():
    return render_template("seller.html")

archive = []

@app.route("/saleposted.html", methods=["POST"])
def addTextbook():
    cNum = request.form['courseNum']
    email = request.form['email']
    name = request.form['textName']
    price = request.form['price']
    addToDatabase(price, cNum, email, name)
    return render_template('saleposted.html')

def addToDatabase(price, cNum, email, name):
    cur.execute("INSERT INTO textbooks (email, courseNum, bookName, price) VALUES ('"+ email +"', '"+ cNum +"', '"+ name +"', "+ price +")")

@app.route("/buyer.html")
def allTextbooks():
	return render_template('buyer.html')

@app.route("/textbooks.html", methods=["POST"])
def searchTextbooks():
	courseNumber = request.form['course']
	cur.execute("SELECT * FROM textbooks WHERE courseNum= '"+ courseNumber+"' ORDER BY price ASC")
    rows = cur.fetchall()
    #return render_template('textbooks.html', rows=rows)
    html = '<html>'
    for(book in rows):
        html.append(book)
    html.append('</html>')
    return html


if __name__ == "__main__":
	app.run(debug=True)

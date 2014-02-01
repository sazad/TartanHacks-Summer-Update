from flask import Flask, request, render_template
import pymysql
app = Flask(__name__)

db = pymysql.connect(host="localhost", user="root", passwd="root", db="textbooks")

cur = db.cursor() 

@app.route("/")
def beginning():
	return render_template('opening.html')

@app.route("/textbook/seller")
def hello():
    return render_template("seller.html")

archive = []

@app.route("/textbook/new", methods=["POST"])
def addTextbook():
    # Print statement here
    print "inside add textbook"
    print request.method
    print "trying forms"
    cNum = request.form['courseNum']
    email = request.form['email']
    name = request.form['textName']
    print cNum
    print email
    print name
    print "printing forms"
    price = request.form['price']
    print price
    addToDatabase(price, cNum, email, name)
    return render_template('saleposted.html')

def addToDatabase(price, cNum, email, name):
    cur.execute("INSERT INTO textbooksNEW (email, courseNum, bookName, price) VALUES ('"+ email +"', '"+ cNum +"', '"+ name +"', "+ price +")")

@app.route("/textbook/buyer")
def allTextbooks():
	return render_template('buyer.html')

@app.route("/textbook/search", methods=["POST"])
def searchTextbooks():
	courseNumber = request.form['course']
	cur.execute("SELECT '"+ courseNumber +"' FROM textbooksNEW WHERE courseNum= '"+ courseNumber+"' ORDER BY price ASC")
	return render_template('textbooks.html', textbooks=cur.fetchall())

class Book:
	def __init__(self, price, course_no,email, name):
		self.price = price
		self.courseNum = course_no
		self.email = email
		self.name = name

if __name__ == "__main__":
	app.run(debug=True)

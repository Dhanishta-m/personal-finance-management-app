from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)


import os

db = pymysql.connect(
    host=os.getenv("DB_HOST","localhost"),
    user=os.getenv("DB_USER","root"),
    password=os.getenv("Dhanishta1810",""),
    database=os.getenv("DB_NAME","finance_db")
)

@app.route('/')
@app.route('/')
def home():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total_expense = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(amount) FROM income")
    total_income = cursor.fetchone()[0] or 0

    cursor.execute("SELECT target_amount FROM budget LIMIT 1")
    budget = cursor.fetchone()[0]

    savings = total_income - total_expense

    return render_template(
        "index.html",
        expenses=expenses,
        total_income=total_income,
        total_expense=total_expense,
        savings=savings,
        budget=budget
    )

@app.route('/add_expense', methods=['POST'])
def add_expense():

    category = request.form['category']
    amount = request.form['amount']

    cursor = db.cursor()

    cursor.execute(
        "INSERT INTO expenses(category, amount) VALUES(%s,%s)",
        (category, amount)
    )

    db.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
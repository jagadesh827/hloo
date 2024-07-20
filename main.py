from flask import Flask, render_template, request, redirect, url_for,flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'


db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='employee_details'
)

@app.route('/')
def index():
    return render_template('index.html',)

@app.route('/add', methods=['POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        position = request.form['position']

        cursor = db.cursor()
        cursor.execute("INSERT INTO employees (name, email, position) VALUES (%s, %s, %s)", (name, email, position))
        db.commit()
        flash('Employee added successfully!', 'success')
    return redirect(url_for('index'))







if __name__ == '__main__':
    app.run(debug=True)

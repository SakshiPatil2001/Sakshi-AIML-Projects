from flask import Flask, render_template, request, redirect
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/book', methods=['GET', 'POST'])
def book_ticket():
    if request.method == 'POST':
        passenger_name = request.form['passenger_name']
        bus_number = request.form['bus_number']
        seat_number = request.form['seat_number']
        date_of_travel = request.form['date_of_travel']

        # Connect to the database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Ensure table name matches your actual table
        cursor.execute('INSERT INTO bookings (passenger_name, bus_number, seat_number, date_of_travel) VALUES (%s, %s, %s, %s)',
               (passenger_name, bus_number, seat_number, date_of_travel))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/confirmation')

    return render_template('book.html')

@app.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')

if __name__ == '__main__':
    app.run(debug=True)

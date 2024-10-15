from flask import Flask, render_template, request
import joblib
import pandas as pd
import mysql.connector

app = Flask(__name__)

# Load the trained model
model = joblib.load(r'C:\Users\saksh\OneDrive\Desktop\zomato-price-prediction\models\zomato_price_predictor.pkl')

# Configure MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sakshi@01",
    database="zomato_db"
)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get form data
        rating = float(request.form['rating'])
        votes = int(request.form['votes'])
        is_veg = 1 if request.form['is_veg'] == 'Yes' else 0

        # Prepare data for prediction
        data = pd.DataFrame([[rating, votes, is_veg]], columns=['rating', 'votes', 'is_veg'])
        predicted_price = model.predict(data)[0]

        # Insert the prediction into MySQL database
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO predictions (rating, votes, is_veg, predicted_price) VALUES (%s, %s, %s, %s)",
            (rating, votes, is_veg, predicted_price)
        )
        db.commit()
        cursor.close()

        return render_template('index.html', prediction=predicted_price)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

 



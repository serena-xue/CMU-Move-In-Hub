import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/choice')
def choice():
    return render_template('choice.html')


@app.route('/short_term')
def short_term():
    hotel_data = pd.read_csv('data/hotel.csv').to_dict(orient='records')
    airbnb_data = pd.read_csv('data/airbnb.csv').to_dict(orient='records')

    return render_template('short_term.html', hotel_data=hotel_data, airbnb_data=airbnb_data)


@app.route('/long_term')
def long_term():
    return "Long Term Housing"


if __name__ == '__main__':
    app.run(debug=True)

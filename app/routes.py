from app import app
from flask import render_template

from app.functions.manipulate_data import data_processing

@app.route('/')
@app.route('/index')
def main_page():
    filename = 'machine_power.csv'
    on_off = data_processing(filename)
    return render_template('index.html', on_off=on_off)
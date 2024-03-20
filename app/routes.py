# from app import app
# from flask import render_template, request

# from app.functions.manipulate_data import data_processing

# @app.route('/', methods=['GET', 'POST']) #Decorades são responsável por informar qual a rota determinada página deve aparecer
# @app.route('/index', methods=['GET', 'POST'])  
# def main_page():      #Função da página principal
#     show_table: bool = False
#     filename: str = 'machine_power.csv'
#     on_off: dict = data_processing(filename)

#     if request.method == 'POST':
#         if ('show-table' in request.form) and (request.form['show-table'] == 'firma01'):
#             show_table = True

#     return render_template('index.html', on_off=on_off, show_table=show_table)  #renderizando a página HTML 

from app import app
from flask import render_template, request

from app.functions.manipulate_data import data_processing

@app.route('/', methods=['GET', 'POST']) 
@app.route('/index', methods=['GET', 'POST'])  
def main_page():
    show_table: bool = False
    filename: str = 'machine_power.csv'
    on_off: dict = data_processing(filename)

    if request.method == 'POST':
        if 'show-table' in request.form:
            if request.form['show-table'] == 'firma01':
                filename = 'machine_power.csv'
            elif request.form['show-table'] == 'firma02':
                filename = 'machine_power2.csv'
            on_off = data_processing(filename)
            show_table = True

    return render_template('index.html', on_off=on_off, show_table=show_table)

from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__, template_folder='resources')
BASE_URL = 'http://numbersapi.com/'


@app.route('/cats', methods=['GET', 'POST'])
def get_cat():
    arg = request.args
    name = arg.get('Name')
    number = arg.get('Number')
    response = requests.get(BASE_URL + number)
    print(number)
    return render_template('cat_picture.html', name=name, text=response.text)


if __name__ == '__main__':
    app.run(port=5000)
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for
import functools
import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/index', methods=['GET', 'POST'])

def index():
    
     
    return render_template("index.html" ) 


if __name__ == "__main__":
    print("Entró en el IF.")
    app.run(debug=True, port=5000)
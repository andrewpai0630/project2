import numpy as np
import sklearn
import sklearn.datasets
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True

@app.route('/send', methods=['GET','POST'])
def main():
    if request.method == 'POST':
        home_team_name = request.form['hometeam']
        away_team_name = request.form['awayteam']
    else:
        return form

if __name__ == "__main__":
    app.run()
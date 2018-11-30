import numpy as np
import sklearn
import sklearn.datasets
import pandas as pd
from flask import Flask, render_template, request
import trained_module
from keras.models import load_model
import numpy as np
import sklearn
import sklearn.datasets
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from keras.utils import to_categorical

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/send', methods=['GET','POST'])
def send():
    if request.method == 'POST':
        home_team_name = request.form['hometeam']
        away_team_name = request.form['awayteam']
    else:
        return render_template("index.html")


nba_model = load_model("NBA_model.h5")

import csv
import os

csvpath = os.path.join("historical_stats.csv")

points_home=[]
rebounds_home=[]
blocks_home=[]
assists_home=[]
fouls_home=[]
turnovers_home=[]

points_away=[]
rebounds_away=[]
blocks_away=[]
assists_away=[]
fouls_away=[]
turnovers_away=[]

home_team_name = app.send.home_team_name
away_team_name = app.send.away_team_name

def gethomeStats(historicalData):
    pointsHome = float(historicalData[23])
    points_home.append(pointsHome)
    print(points_home)
    
    reboundsHome = float(historicalData[17])
    rebounds_home.append(reboundsHome)
    print(rebounds_home)    

    blocksHome = float(historicalData[20])
    blocks_home.append(blocksHome)
    print(blocks_home) 
    
    assistsHome = float(historicalData[18])
    assists_home.append(assistsHome)
    print(assists_home)     

    fouls_Home = float(historicalData[22])
    fouls_home.append(fouls_Home)
    print(fouls_home)    
    
    turnovers_Home = float(historicalData[21])
    turnovers_home.append(turnovers_Home)
    print(turnovers_home)
    
def getawayStats(historicalData):
    pointsAway = float(historicalData[23])
    points_away.append(pointsAway)
    print(points_away)
    
    reboundsAway = float(historicalData[17])
    rebounds_away.append(reboundsAway)
    print(rebounds_away)    

    blocksAway = float(historicalData[20])
    blocks_away.append(blocksAway)
    print(blocks_away) 
    
    assistsAway = float(historicalData[18])
    assists_away.append(assistsAway)
    print(assists_away)     

    fouls_Away = float(historicalData[22])
    fouls_away.append(fouls_Away)
    print(fouls_away)    
    
    turnovers_Away = float(historicalData[21])
    turnovers_away.append(turnovers_Away)
    print(turnovers_away)


with open(csvpath, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'getPercentages()' function
        if(home_team_name == row[0]):
            gethomeStats(row)
            
        if(away_team_name == row[0]):
            getawayStats(row)

new_data = np.array([[points_home[0],assists_home[0], blocks_home[0], rebounds_home[0], turnovers_home[0], fouls_home[0],points_away[0],assists_away[0], blocks_away[0], rebounds_away[0], turnovers_away[0], fouls_away[0]]])

final_encoded_prediction = nba_model.predict_classes(new_data)
if (final_encoded_prediction >0):
    print("Home Team Win")
else:
    print("Home Team Lose")

if __name__ == "__main__":
    app.run()
#python flask application for the user...........

from flask import Flask, jsonify

import requests

import csv

from io import StringIO


app = Flask(__name__)

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/08-22-2020.csv"

countries = ["Ghana", "Togo"]

covid_cases = []



@app.route("/api")
def index():

    resp = requests.get(url)

    data = resp.content.decode("ascii", "ignore")

    csv_data = StringIO(data)

    reader = csv.reader(csv_data)

    for row in reader:
        if row[0] == "FIPS":
            continue
        if row[3] in countries:
            covid_cases.append({
                "country": row[3],
                "confirmed cases": row[7],
                "deaths": row[8],
                "recoveries": row[9],
                "active cases": row[10]
            })


    print(covid_cases)
    return jsonify({"Covid 19 cases": [
        {"Country": "USA", "Reported cases": 120000},
        {"Country": "China", "Reported cases": 82000},
        {"Country": "Korea", "Reported cases": 12000},
        {"Country": "Ghana", "Reported cases": 2500},
        
        ]})



if __name__ == "__main__":
    app.run(port=2000, debug=True)
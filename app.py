from flask import Flask, render_template, request
import requests
import weather

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        city_name = request.form.get("city")
        print(city_name)
        data = weather.weather_fetch(city_name)
    return render_template("index.html")

app.run(debug=True)
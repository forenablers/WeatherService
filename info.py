import requests
import json
from flask import Flask
from flask import request
import json

with open('config.json', 'r') as f:
    config = json.load(f)

appId = config['Default']['APPID'] # 'secret-key-of-myapp'

app = Flask(__name__)

@app.route('/weather')
def getWeather():
    print appId
    city = request.args.get('city')
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q={0}&appid={1}&units=metric'.format(city, appId)).content
    weather = json.loads(response)
    return 'The weather in {0} is {1}'.format(city, weather["main"]["temp"])

if __name__ == "__main__":
    app.run()
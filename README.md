
## Get APPID
First of all you will need to specify an `APPID` in the `config.json`. The `APPID` you can get after registration [here](https://openweathermap.org/forecast5)

## Build & run image
In order to build and run it, execute:

 ```bash
 docker build -t weather-service .
 docker run -d -p 5000:5000  weather-service
 ```

## Use it
 To use it go to [http://localhost:5000/weather?city=Amsterdam](http://localhost:5000/weather?city=Amsterdam).
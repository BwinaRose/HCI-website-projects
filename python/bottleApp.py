from bottle import route, run, view, static_file, get, post, request, template
from datetime import datetime
import pytz
import requests
from animePics import pics
import random
import APIkey as api


@route('/')
@route('/home')
def main():
    return static_file("home.html", root="pages/")


@route('/projects')
@view("projects")
def redirecting():
    return static_file("projects.html", root="pages/")



@route('/weather')
@view("pages/weatherHard")
def weather():
    city = "Dover"
    state = "DE"
    city2 = "Dallas"
    state2 = "TX"
    country = "us"
    city3 = "Tokyo"
    country2 = "jp"

    APIkey = api.APIkey

    call = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={APIkey}&units=imperial"
    response = requests.get(call)
    jsonData = response.json()
    call1_2 = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid={APIkey}&units=metric"
    response1_2 = requests.get(call1_2)
    jsonData1_2 = response1_2.json()
    data1_2 = jsonData1_2["main"]
    jsonWeather = jsonData["weather"]
    data = jsonData["main"]

    call2 = f"https://api.openweathermap.org/data/2.5/weather?q={city2},{state2},{country}&appid={APIkey}&units=imperial"
    response2 = requests.get(call2)
    jsonData2 = response2.json()
    jsonWeather2 = jsonData2["weather"]
    call2_2 = f"https://api.openweathermap.org/data/2.5/weather?q={city2},{state2},{country}&appid={APIkey}&units=metric"
    response2_2 = requests.get(call2_2)
    jsonData2_2 = response2_2.json()
    data2_2 = jsonData2_2["main"]
    data2 = jsonData2["main"]
    icon = jsonWeather[0]["icon"]
    icon2 = jsonWeather2[0]["icon"]

    call3 = f"https://api.openweathermap.org/data/2.5/weather?q={city3},{country2}&appid={APIkey}&units=imperial"
    response3 = requests.get(call3)
    jsonData3 = response3.json()
    jsonWeather3 = jsonData3["weather"]
    call3_2 = f"https://api.openweathermap.org/data/2.5/weather?q={city3},{country2}&appid={APIkey}&units=metric"
    response3_2 = requests.get(call3_2)
    jsonData3_2 = response3_2.json()
    data3_2 = jsonData3_2["main"]
    data3 = jsonData3["main"]
    icon3 = jsonWeather3[0]["icon"]

    local = pytz.timezone('US/Eastern')
    naive = datetime.now()
    local_dt = local.localize(naive)
    utc_dt = local_dt.astimezone(pytz.utc)

    tz0 = pytz.timezone('US/Eastern')
    est_dt = utc_dt.astimezone(tz0)
    tz = pytz.timezone('US/Central')
    cst_dt = utc_dt.astimezone(tz)

    tz2 = pytz.timezone('Asia/Tokyo')
    jp_dt = utc_dt.astimezone(tz2)
    return dict(
        APIkey=api.APIkey,

        city="Dover",
        state="DE",
        est_time=est_dt.strftime("%b %d, %Y  %I:%M:%S %p"),
        currentTemp=data["temp"],
        currentTempC=data1_2["temp"],
        description=jsonWeather[0]["description"],
        icon=jsonWeather[0]["icon"],
        iconCall=f"http://openweathermap.org/img/wn/{icon}@2x.png",

        city2="Dallas",
        state2="TX",
        cst_time=cst_dt.strftime("%b %d, %Y  %I:%M:%S %p"),
        currentTemp2=data2["temp"],
        currentTempC2=data2_2["temp"],
        description2=jsonWeather2[0]["description"],
        icon2=jsonWeather2[0]["icon"],
        iconCall2=f"http://openweathermap.org/img/wn/{icon2}@2x.png",

        city3="Tokyo",
        country2="Japan",
        jp_time=jp_dt.strftime("%b %d, %Y  %I:%M:%S %p"),
        currentTemp3=data3["temp"],
        currentTempC3=data3_2["temp"],
        description3=jsonWeather3[0]["description"],
        icon3=jsonWeather3[0]["icon"],
        iconCall3=f"http://openweathermap.org/img/wn/{icon3}@2x.png",
    )


@route('/change/<coins>')
@view("pages/midterms/coins")
def change(coins):
    return dict(
        coins=coins,
        quarterImg="../../static/assets/quarter.png",
        dimeImg="../../static/assets/dime.png",
        nickelImg="../../static/assets/nickel.png",
        pennyImg="../../static/assets/penny.png"
    )


@route('/multiple')
@view("pages/midterms/multiple")
def table():
    return dict(
        row=10, col=10)


@route('/factors/<num>')
@view("pages/midterms/factors")
def factor(num):
    return dict(num=num)


@route('/imperial')
@view("pages/midterms/imperial")
def imperial():
    return dict(
        inches=12, feet=9
    )


@route('/max/<nums>')
@view("pages/midterms/max")
def maximum(nums):
    return dict(nums=nums)


@route('/sum/<num>')
@view("pages/midterms/sum")
def sumNum(num):
    return dict(num=num)


@route('/quote')
@view("pages/midterms/quote")
def tempEx():
    return dict(borderSize=7,
                borderColor="#ffa2e1",
                backgroundColor="teal")


@route('/quote2')
@view("pages/midterms/quote")
def tempEx():
    return dict(borderSize=15,
                borderColor="#4a148c",
                backgroundColor="#E1A174")


@route('/quote3')
@view("pages/midterms/quote")
def tempEx():
    return dict(borderSize=2,
                borderColor="black",
                backgroundColor="lightblue")


@route('/anime')
@view("pages/anime")
def anime():
    call = "https://animechan.vercel.app/api/random"
    response = requests.get(call)
    jsonData = response.json()
    quoteAni = jsonData["anime"]
    spokenBy = jsonData["character"]
    quote = jsonData["quote"]
    imageIndex = random.randint(0, len(pics) - 1)
    image = pics[imageIndex]
    return dict(image=image,
                quoteAni=quoteAni,
                spokenBy=spokenBy,
                quote=quote)


# editing weather for user input

@get('/weather2')
@view("pages/weatherForm")
def weatherForm():
    city = None
    state = None
    return template("pages/weatherForm", city=city, state=state)


@post('/weather2')
@view("pages/weatherOut")
def weatherOut():
    city = request.forms.get('city')
    state = request.forms.get('state')
    country = "us"
    APIkey = api.APIkey

    currentcall = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&appid" \
              f"={APIkey}&units=imperial"
    currentresponse = requests.get(currentcall)
    jsonData = currentresponse.json()
    jsonWeather = jsonData["weather"]
    data = jsonData["main"]
    currentTemp=round(data["temp"])
    max=round(data["temp_max"])
    min=round(data["temp_min"])
    mainWeather = jsonWeather[0]["main"]
    icon = jsonWeather[0]["icon"]

    coordCall = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},{country}&appid={APIkey}"
    coordResponse = requests.get(coordCall)
    coordData = coordResponse.json()
    data2 =coordData[0]
    lat = data2["lat"]
    lon = data2["lon"]
    # print(coordData)

    mainCall = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=minutely,alerts," \
               f"hourly&appid" \
               f"={APIkey}&units=imperial"
    mainresponse = requests.get(mainCall)
    maindata = mainresponse.json()
    dailyData = maindata["daily"]

    day0 = dailyData[0]
    current_utc = maindata["current"]["dt"]
    sunrise_utc = day0["sunrise"]
    sunset_utc = day0["sunset"]

    # day0 "TODAY"
    day1 = dailyData[1]
    day2 = dailyData[2]
    day3 = dailyData[3]
    day4 = dailyData[4]
    day5 = dailyData[5]
    # dt4 = datetime.fromtimestamp(day4["dt"])
    # get day of the week (MTWRFSS)

    # if dt > (sunrise+3600) && dt < (sunset-3600)
    #  == day
    # elif dt < (sunrise+3600) && st > (sunset-3600)
    #  == night
    # else
    #  == sunrise/sunset

    if (mainWeather == "Thunderstorm"):
        print(mainWeather)
        if (current_utc > sunrise_utc+3600 and current_utc < sunset_utc-3600):
            print("day")
            bgimg="../static/assets/weatherbg/thunder-day.gif"
        elif (current_utc < sunrise_utc+3600 and current_utc > sunset_utc-3600):
            print("night")
            bgimg="../static/assets/weatherbg/thunder-night.gif"
        elif ((current_utc == sunrise_utc or current_utc <= sunrise_utc+3600) or (current_utc == sunset_utc or
                                                                                  current_utc >= sunrise_utc-3600)):
            print("sunset/sunrise")
            bgimg="../static/assets/weatherbg/thunder-sun.gif"
    elif (mainWeather == "Drizzle"):
        print(mainWeather)
        if (current_utc > sunrise_utc+3600 and current_utc < sunset_utc-3600):
            print("day")
            bgimg="../static/assets/weatherbg/drizzle-day.gif"
        elif (current_utc < sunrise_utc+3600 and current_utc > sunset_utc-3600):
            print("night")
            bgimg="../static/assets/weatherbg/drizzle-night.gif"
        elif ((current_utc == sunrise_utc or current_utc <= sunrise_utc+3600) or (current_utc == sunset_utc or
                                                                                  current_utc >= sunrise_utc-3600)):
            print("sunset/sunrise")
            bgimg="../static/assets/weatherbg/drizzle-sun.gif"
    elif (mainWeather == "Rain"):
        print(mainWeather)
        if (current_utc > sunrise_utc+3600 and current_utc < sunset_utc-3600):
            print("day")
            bgimg="../static/assets/weatherbg/rain-day.gif"
        elif (current_utc < sunrise_utc+3600 and current_utc > sunset_utc-3600):
            print("night")
            bgimg="../static/assets/weatherbg/rain-night.gif"
        elif ((current_utc == sunrise_utc or current_utc <= sunrise_utc+3600) or (current_utc == sunset_utc or
                                                                                  current_utc >= sunrise_utc-3600)):
            print("sunset/sunrise")
            bgimg="../static/assets/weatherbg/rain-sun.gif"
    elif (mainWeather == "Snow"):
        print(mainWeather)
        if (current_utc > sunrise_utc+3600 and current_utc < sunset_utc-3600):
            print("day")
            bgimg="../static/assets/weatherbg/snow-day.gif"
        elif (current_utc < sunrise_utc+3600 and current_utc > sunset_utc-3600):
            print("night")
            bgimg="../static/assets/weatherbg/snow-night.gif"
        elif ((current_utc == sunrise_utc or current_utc <= sunrise_utc+3600) or (current_utc == sunset_utc or
                                                                                  current_utc >= sunrise_utc-3600)):
            print("sunset/sunrise")
            bgimg="../static/assets/weatherbg/snow-sun.gif"
    elif (mainWeather == "Mist" or mainWeather == "Smoke" or mainWeather == "Haze" or mainWeather == "Dust" or
          mainWeather == "Fog" or mainWeather == "Sand" or mainWeather == "Ash" or mainWeather == "Squall" or
          mainWeather == "Tornado"):
        print(mainWeather)
        if (current_utc > sunrise_utc+3600 and current_utc < sunset_utc-3600):
            print("day")
            bgimg="../static/assets/weatherbg/mist-day.gif"
        elif (current_utc < sunrise_utc+3600 and current_utc > sunset_utc-3600):
            print("night")
            bgimg="../static/assets/weatherbg/mist-night.gif"
        elif ((current_utc == sunrise_utc or current_utc <= sunrise_utc+3600) or (current_utc == sunset_utc or
                                                                                  current_utc >= sunrise_utc-3600)):
            print("sunset/sunrise")
            bgimg="../static/assets/weatherbg/mist-sun.gif"
    elif (mainWeather == "Clear"):
        print(mainWeather)
        if (current_utc > sunrise_utc+3600 and current_utc < sunset_utc-3600):
            print("day")
            bgimg="../static/assets/weatherbg/clear-day.gif"
        elif (current_utc < sunrise_utc+3600 and current_utc > sunset_utc-3600):
            print("night")
            bgimg="../static/assets/weatherbg/clear-night.gif"
        elif ((current_utc == sunrise_utc or current_utc <= sunrise_utc+3600) or (current_utc == sunset_utc or
                                                                                  current_utc >= sunrise_utc-3600)):
            print("sunset/sunrise")
            bgimg="../static/assets/weatherbg/clear-sun.gif"
    elif (mainWeather == "Clouds"):
        print(mainWeather)
        if (current_utc > sunrise_utc+3600 and current_utc < sunset_utc-3600):
            print("day")
            bgimg="../static/assets/weatherbg/cloud-day.gif"
        elif (current_utc < sunrise_utc+3600 and current_utc > sunset_utc-3600):
            print("night")
            bgimg="../static/assets/weatherbg/cloud-night.gif"
        elif ((current_utc == sunrise_utc or current_utc <= sunrise_utc+3600) or (current_utc == sunset_utc or
                                                                                  current_utc >= sunrise_utc-3600)):
            print("sunset/sunrise")
            bgimg="../static/assets/weatherbg/cloud-sun.gif"
    else:
        print("Error")

    return dict(currentTemp=currentTemp,
                max=max,
                min=min,
                city=city,
                state=state,
                description=jsonWeather[0]["description"],
                iconCall=f"https://openweathermap.org/img/wn/{icon}@2x.png",
                mainWeather=mainWeather,
                bgimg=bgimg)
# sabrina krueger


@route('/pages/<filename>')
def send_pages(filename):
    return static_file(f'{filename}.html', root='pages')


@route('/static/assets/<filename>')
def send_assets(filename):
    return static_file(f'{filename}', root='static/assets')


@route('/static/assets/weatherbg/<filename>')
def send_weatherbg(filename):
    return static_file(f'{filename}', root='static/assets/weatherbg')


@route('/static/css/style.css')
def send_css():
    return static_file("style.css", "static/css")


@route('/static/css/mapstyle.css')
def send_css2():
    return static_file("mapstyle.css", "static/css")


run(host='localhost', port=8085, debug=True, reloader=True)

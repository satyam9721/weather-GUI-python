import tkinter as tk  #tkinter is used to create Gui app
import requests      #The requests module allows you to send HTTP requests using Python.
import time         #time keyword use for the time feching

#tkinter,requests,time are module

#we use postman api reader,to anylaize the api

#all data is used,it's required,because it's throw the error

#getWeather function display the whole contain of our weather app


def getWeather(canvas):
    city = textField.get()  #taking the name of city
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=c048b6bf0734817fcbdf882055d01910"

    # api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    # api picked from https://home.openweathermap.org/
    # textField's city name goes into that variables

    #in all below  line main,temp,temp_min,temp_max,pressure,humidity,speed,sunrise,sunset    are chacter present in api show ,we using it.

    json_data = requests.get(api).json()   #to send data request to api

    condition = json_data['weather'][0]['main']   #recieved data from api

    temp = int(json_data['main']['temp'] - 273.15)  #api giving tempreature in kelvin ,then subtrac(-273.15),data is float format then converting in to integer by(int)

    min_temp = int(json_data['main']['temp_min'] - 273.15)    #minimum temprature, from api,,recieved data from api

    max_temp = int(json_data['main']['temp_max'] - 273.15)  # max_temperature from api,recieved data from api

    pressure = json_data['main']['pressure']  # pressure from api ,recieved data from api

    humidity = json_data['main']['humidity']  # hunidity from api,recieved data from api

    wind = json_data['wind']['speed']     #this line states that api give the wind spped

#strftime() function is used to convert date and time objects to their string representation
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21000))  #sunrise time in second ,according to india gmt 5:30converting in proper time by (- 19,080)

    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21000))   #sunset time in second ,converting in propertime by

    final_info = condition + "\n" + str(temp) + "°C"   #str(temp) has temparature in string format / data is converted to string

    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    #tempreatur ,pressure etc ,GUI mai show hua

    label1.config(text=final_info)

    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("800x500")  #window size
canvas.title("Weather App")  #app name
f = ("poppins", 15, "bold")  #textstyle
t = ("poppins", 35, "bold")    #text  style

textField = tk.Entry(canvas, justify='center', width=20, font=t)

textField.pack(pady=20)

textField.focus()

textField.bind('<Return>', getWeather)  #if you hit enter button, then it's shows location information

label1 = tk.Label(canvas, font=t)

label1.pack()

label2 = tk.Label(canvas, font=f)

label2.pack()

canvas.mainloop()

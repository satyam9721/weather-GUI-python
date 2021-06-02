import tkinter as tk  #tkinter is used to create Gui app
import requests      #The requests module allows you to send HTTP requests using Python.
import time         #time keyword use for the time feching

#tkinter,requests,time are module

#we use postman api reader,to anylaize the api

#jitna data api de rahi, vo sab ko use kro warna error ayega

#getWeather function display the whole contain of our weather app


def getWeather(canvas):
    city = textField.get()  #taking the name of city
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=c048b6bf0734817fcbdf882055d01910"

    # api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    # api yaha se liya https://home.openweathermap.org/
    # textField se jo city ka name aya wahi city mai jayega

    #in all below  line main,temp,temp_min,temp_max,pressure,humidity,speed,sunrise,sunset    are chacter present in api show ,we using it.

    json_data = requests.get(api).json()   #api  ko data ki request bhej raha hai

    condition = json_data['weather'][0]['main']   #api  ko data ki request bhej raha hai /api se yaha data liye

    temp = int(json_data['main']['temp'] - 273.15)  #api giving tempreature in kelvin ,then subtrac(-273.15),data is float format then converting in to integer by(int)

    min_temp = int(json_data['main']['temp_min'] - 273.15)    #minimum temprature, from api,,api se yaha data liye

    max_temp = int(json_data['main']['temp_max'] - 273.15)  # max_temperature from api,api se yaha data liye

    pressure = json_data['main']['pressure']  # pressure from api ,api se yaha data liye

    humidity = json_data['main']['humidity']  # hunidity from api,api se yaha data liye

    wind = json_data['wind']['speed']     #this line api se is file mai location ki speed ka weather ka data liyi from api

#strftime() function is used to convert date and time objects to their string representation
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21000))  #sunrise time in second ,according to india gmt 5:30converting in proper time by (- 19,080)

    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21000))   #sunset time in second ,converting in propertime by

    final_info = condition + "\n" + str(temp) + "°C"   #str(temp) has temparature in string format / data ko string mai change kiya

    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset

    #final_data variable mai likhi chezz se hi ,tempreatur ,pressure etc ,GUI mai show hua

    label1.config(text=final_info)

    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("800x500")  #window ka size
canvas.title("Weather App")  #app ka name
f = ("poppins", 15, "bold")  #text ka style
t = ("poppins", 35, "bold")    #text ka style

textField = tk.Entry(canvas, justify='center', width=20, font=t)

textField.pack(pady=20)

textField.focus()

textField.bind('<Return>', getWeather)  #app mai enter marne se ,location ka information dega

label1 = tk.Label(canvas, font=t)

label1.pack()

label2 = tk.Label(canvas, font=f)

label2.pack()

canvas.mainloop()

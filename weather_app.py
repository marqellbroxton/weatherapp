import tkinter as tk
import requests
import time


def get_weather(self):
    city = text_field.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=ff987ab817d72e828417bee6d123720e"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 221.15)
    min_temp = int(json_data['main']['temp_min'] - 221.15)
    max_temp = int(json_data['main']['temp_max'] - 221.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise']))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset']))

    final_info = condition + "\n" + str(temp) + "°F"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp)\
                 + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity)\
                 + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + str(sunrise) + "\n" + "Sunset: " + str(sunset)
    label1.config(text=final_info)
    label2.config(text=final_data)


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

text_field = tk.Entry(canvas, font=t)
text_field.pack(pady=20)
text_field.focus()
text_field.bind('<Return>', get_weather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()


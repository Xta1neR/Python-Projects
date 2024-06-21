import requests
import win32com.client as wincom
import time
import tkinter as tk
from tkinter import messagebox

def fetch_weather():
    city = city_entry.get()
    url = f"https://api.weatherapi.com/v1/current.json?key=3202d8863f524a80b23135148242006&q={city}"

    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for non-200 status codes

        data = r.json()

        condition = data['current']['condition']['text']
        temp_c = data['current']['temp_c']
        humidity = data['current']['humidity']
        wind_mph = data['current']['wind_mph']

        result_label.config(text=f"Current weather in {city}:\n"
        	f"Condition: {condition}\n"
        	f"Temperature: {temp_c} °C\n"
        	f"Humidity: {humidity} %\n"
        	f"Wind Speed: {wind_mph} mph")

        speak = wincom.Dispatch("SAPI.SpVoice")
        speak.Speak(f"Current weather in {city}:")
        time.sleep(1)
        speak.Speak(f"Condition: {condition}")
        time.sleep(1)
        speak.Speak(f"Temperature: {temp_c} degrees Celsius")
        time.sleep(1)
        speak.Speak(f"Humidity: {humidity} percent")
        time.sleep(1)
        speak.Speak(f"Wind Speed: {wind_mph} miles per hour")
        time.sleep(1)
        speak.Speak("Thank you for using the weather app. Goodbye!")

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred while fetching weather data: {e}")

    except KeyError:
        messagebox.showerror("Error", f"Unable to find weather data for '{city}'. Please check the city name and try again.")

# Create the main window
root = tk.Tk()
root.title("Weather App")

# City entry
city_label = tk.Label(root, text="Enter city:")
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=30)
city_entry.pack()

# Fetch weather button
fetch_button = tk.Button(root, text="Fetch Weather", command=fetch_weather)
fetch_button.pack(pady=10)

# Result label (to display weather information)
result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=20)

# Run the main loop
root.mainloop()

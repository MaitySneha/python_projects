from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from tkinter import messagebox

class WeatherApp:
    def fetch_weather(self):
        city = self.city_combobox.get()
        api_key = 'abe59e596e95e501f4c3ff4e463fa60d'  # Replace with your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(url)
            data = response.json()
            if data['cod'] == 200:
                self.display_weather(data)
            else:
                messagebox.showerror("Error", f"City not found: {city}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def display_weather(self, data):
        city_name = data['name']
        country = data['sys']['country']
        temperature_c = round(data['main']['temp'] - 273.15, 2)
        weather = data['weather'][0]['main']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        self.location_label.config(text=f"📍 {city_name}, {country}")
        self.temp_label.config(text=f"🌡️ {temperature_c}°C")
        self.weather_label.config(text=f"☁️ {weather}")
        self.humidity_label.config(text=f"💧 Humidity: {humidity}%")
        self.wind_label.config(text=f"🍃 Wind Speed: {wind_speed} m/s")

        # AI-generated weather advice
        advice = "Stay hydrated!" if temperature_c > 30 else "Wear warm clothes!" if temperature_c < 15 else "Enjoy the pleasant weather!"
        self.advice_label.config(text=f"🤖 Advice: {advice}")

        # Dynamic background and animations
        bg_color = "#ffcccb" if temperature_c > 30 else "#add8e6" if temperature_c < 15 else "#F7A5A9"
        self.root.config(bg=bg_color)
        self.animate_details()

    def animate_details(self):
        for widget in self.details_frame.winfo_children():
            widget.pack_forget()
        for widget in self.details_frame.winfo_children():
            widget.pack(anchor=W, pady=5)

    def __init__(self):
        self.root = Tk()
        self.root.title("Stylish Weather App")
        self.root.geometry("800x600")
        self.root.config(bg="#F7A5A9")

        # Header Section
        header = Frame(self.root, bg="#444466", height=80)
        header.pack(fill=X)

        app_title = Label(header, text="🌤️ Weather Application", fg="white", bg="#444466", font=("Verdana", 20, "bold"))
        app_title.pack(pady=10)

        # Current Date
        date_label = Label(header, text=datetime.now().strftime('%Y-%m-%d'), fg="white", bg="#444466", font=("Verdana", 12))
        date_label.pack(anchor=E, padx=10)

        # Search Section
        search_frame = Frame(self.root, bg="#2d2d44")
        search_frame.pack(pady=30)

        city_label = Label(search_frame, text="🌍 Select City:", fg="white", bg="#2d2d44", font=("Verdana", 14))
        city_label.grid(row=0, column=0, padx=10, pady=10)

        self.city_combobox = ttk.Combobox(search_frame, font=("Verdana", 14), width=30)
        self.city_combobox["values"] = ["London", "Paris", "New York", "Tokyo", "Mumbai", "Sydney","Kolkata","Haldia"]
        self.city_combobox.grid(row=0, column=1, padx=10, pady=10)

        search_button = Button(search_frame, text="Search 🔍", bg="#5e5ec2", fg="white", font=("Verdana", 14, "bold"), command=self.fetch_weather)
        search_button.grid(row=0, column=2, padx=10, pady=10)

        search_button.bind("<Enter>", lambda e: search_button.config(bg="#4b4bb2"))
        search_button.bind("<Leave>", lambda e: search_button.config(bg="#5e5ec2"))

        # Weather Details Section
        self.details_frame = Frame(self.root, bg="#2d2d44", bd=5, relief=RIDGE)
        self.details_frame.pack(pady=30, padx=20)

        self.location_label = Label(self.details_frame, text="📍 Location: N/A", fg="white", bg="#2d2d44", font=("Verdana", 16, "bold"))
        self.location_label.pack(anchor=W, pady=5)

        self.temp_label = Label(self.details_frame, text="🌡️ Temperature: N/A", fg="white", bg="#2d2d44", font=("Verdana", 14))
        self.temp_label.pack(anchor=W, pady=5)

        self.weather_label = Label(self.details_frame, text="☁️ Weather: N/A", fg="white", bg="#2d2d44", font=("Verdana", 14))
        self.weather_label.pack(anchor=W, pady=5)

        self.humidity_label = Label(self.details_frame, text="💧 Humidity: N/A", fg="white", bg="#2d2d44", font=("Verdana", 14))
        self.humidity_label.pack(anchor=W, pady=5)

        self.wind_label = Label(self.details_frame, text="🍃 Wind Speed: N/A", fg="white", bg="#2d2d44", font=("Verdana", 14))
        self.wind_label.pack(anchor=W, pady=5)

        self.advice_label = Label(self.details_frame, text="🤖 Advice: N/A", fg="white", bg="#2d2d44", font=("Verdana", 14, "italic"))
        self.advice_label.pack(anchor=W, pady=10)

        # Footer
        footer = Label(self.root, text="Made by Sneha", bg="#2d2d44", fg="white", font=("Verdana", 12))
        footer.pack(side=BOTTOM, pady=10)

        self.root.mainloop()

if __name__ == '__main__':
    WeatherApp()

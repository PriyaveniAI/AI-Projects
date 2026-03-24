# ============================================
# P4 Weather App - No API Key Required!
# ============================================

import tkinter as tk
from tkinter import scrolledtext
import urllib.request
import json
import datetime

# ---- Weather Data (No API Key Needed!) ----

def get_weather(city):
    try:
        # Using wttr.in - completely free, no API key needed!
        city_encoded = city.replace(" ", "+")
        url = f"https://wttr.in/{city_encoded}?format=j1"
        
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=10)
        data = json.loads(response.read().decode())
        
        # Extract weather info
        current = data['current_condition'][0]
        area = data['nearest_area'][0]
        
        city_name = area['areaName'][0]['value']
        country = area['country'][0]['value']
        temp_c = current['temp_C']
        temp_f = current['temp_F']
        feels_like = current['FeelsLikeC']
        humidity = current['humidity']
        wind_speed = current['windspeedKmph']
        description = current['weatherDesc'][0]['value']
        visibility = current['visibility']
        
        # Weather emoji
        desc_lower = description.lower()
        if 'sun' in desc_lower or 'clear' in desc_lower:
            emoji = '☀️'
        elif 'cloud' in desc_lower or 'overcast' in desc_lower:
            emoji = '☁️'
        elif 'rain' in desc_lower or 'drizzle' in desc_lower:
            emoji = '🌧️'
        elif 'thunder' in desc_lower or 'storm' in desc_lower:
            emoji = '⛈️'
        elif 'snow' in desc_lower or 'blizzard' in desc_lower:
            emoji = '❄️'
        elif 'fog' in desc_lower or 'mist' in desc_lower:
            emoji = '🌫️'
        elif 'wind' in desc_lower:
            emoji = '💨'
        elif 'partly' in desc_lower:
            emoji = '⛅'
        else:
            emoji = '🌤️'
        
        result = f"""
{emoji} Weather in {city_name}, {country}
{'='*40}
🌡️  Temperature:  {temp_c}°C / {temp_f}°F
🤔  Feels Like:   {feels_like}°C
📝  Condition:    {description}
💧  Humidity:     {humidity}%
💨  Wind Speed:   {wind_speed} km/h
👁️  Visibility:   {visibility} km
{'='*40}
🕐  Updated: {datetime.datetime.now().strftime("%I:%M %p")}
        """
        return result
        
    except urllib.error.URLError:
        return "❌ No internet connection! Please check your internet and try again."
    except Exception as e:
        return f"❌ City not found! Please check the city name and try again.\nTip: Try 'London', 'Mumbai', 'New York'"


def search_weather():
    city = entry.get().strip()
    if not city:
        result_area.config(state=tk.NORMAL)
        result_area.delete(1.0, tk.END)
        result_area.insert(tk.END, "⚠️ Please enter a city name!", "warning")
        result_area.config(state=tk.DISABLED)
        return
    
    # Show loading
    result_area.config(state=tk.NORMAL)
    result_area.delete(1.0, tk.END)
    result_area.insert(tk.END, f"🔍 Searching weather for {city}...", "loading")
    result_area.config(state=tk.DISABLED)
    window.update()
    
    # Get weather
    weather = get_weather(city)
    
    result_area.config(state=tk.NORMAL)
    result_area.delete(1.0, tk.END)
    result_area.insert(tk.END, weather, "result")
    result_area.config(state=tk.DISABLED)


def clear_search():
    entry.delete(0, tk.END)
    result_area.config(state=tk.NORMAL)
    result_area.delete(1.0, tk.END)
    result_area.insert(tk.END, "🌍 Enter a city name above to get weather!", "welcome")
    result_area.config(state=tk.DISABLED)
    entry.focus()


# ---- Build Window ----

window = tk.Tk()
window.title("🌤️ Weather App")
window.geometry("480x550")
window.configure(bg="#0f172a")
window.resizable(False, False)

# Header
header = tk.Frame(window, bg="#3b82f6", pady=15)
header.pack(fill=tk.X)

tk.Label(header, text="🌤️ Weather App", font=("Arial", 20, "bold"),
         bg="#3b82f6", fg="white").pack()
tk.Label(header, text="No API Key Required ✅", font=("Arial", 10),
         bg="#3b82f6", fg="#bfdbfe").pack()

# Search Frame
search_frame = tk.Frame(window, bg="#0f172a", pady=15)
search_frame.pack(fill=tk.X, padx=20)

tk.Label(search_frame, text="Enter City Name:", font=("Arial", 11, "bold"),
         bg="#0f172a", fg="#94a3b8").pack(anchor="w")

input_row = tk.Frame(search_frame, bg="#0f172a")
input_row.pack(fill=tk.X, pady=5)

entry = tk.Entry(input_row, font=("Arial", 13), bg="#1e293b", fg="white",
                 insertbackground="white", relief=tk.FLAT, bd=8)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
entry.bind("<Return>", lambda e: search_weather())
entry.focus()

search_btn = tk.Button(input_row, text="Search 🔍", font=("Arial", 11, "bold"),
                       bg="#3b82f6", fg="white", relief=tk.FLAT, cursor="hand2",
                       padx=12, pady=8, command=search_weather)
search_btn.pack(side=tk.RIGHT, padx=(8, 0))

# Quick city buttons
quick_frame = tk.Frame(window, bg="#0f172a")
quick_frame.pack(fill=tk.X, padx=20)

tk.Label(quick_frame, text="Quick Search:", font=("Arial", 10, "bold"),
         bg="#0f172a", fg="#94a3b8").pack(anchor="w")

cities_row = tk.Frame(quick_frame, bg="#0f172a")
cities_row.pack(fill=tk.X, pady=4)

for city in ["Chennai", "Mumbai", "Delhi", "London", "New York"]:
    btn = tk.Button(cities_row, text=city, font=("Arial", 9, "bold"),
                    bg="#1e293b", fg="#93c5fd", relief=tk.FLAT, cursor="hand2",
                    padx=8, pady=4,
                    command=lambda c=city: [entry.delete(0, tk.END),
                                            entry.insert(0, c),
                                            search_weather()])
    btn.pack(side=tk.LEFT, padx=2)

# Result Area
result_frame = tk.Frame(window, bg="#0f172a", pady=10)
result_frame.pack(fill=tk.BOTH, expand=True, padx=20)

result_area = scrolledtext.ScrolledText(result_frame, wrap=tk.WORD,
                                         state=tk.DISABLED,
                                         font=("Courier", 11),
                                         bg="#1e293b", fg="white",
                                         insertbackground="white",
                                         padx=15, pady=15,
                                         relief=tk.FLAT)
result_area.pack(fill=tk.BOTH, expand=True)
result_area.tag_config("welcome", foreground="#94a3b8", font=("Arial", 12))
result_area.tag_config("loading", foreground="#fbbf24", font=("Arial", 12))
result_area.tag_config("result", foreground="#86efac", font=("Courier", 11))
result_area.tag_config("warning", foreground="#f87171", font=("Arial", 12))

# Welcome message
result_area.config(state=tk.NORMAL)
result_area.insert(tk.END, "🌍 Enter a city name above to get weather!\n\nTip: Click any city button for quick search!", "welcome")
result_area.config(state=tk.DISABLED)

# Clear button
clear_btn = tk.Button(window, text="Clear 🗑️", font=("Arial", 10, "bold"),
                      bg="#1e293b", fg="#94a3b8", relief=tk.FLAT,
                      cursor="hand2", padx=10, pady=6, command=clear_search)
clear_btn.pack(pady=(0, 10))

# Footer
tk.Label(window, text="Powered by wttr.in | No API Key Needed",
         font=("Arial", 8), bg="#0f172a", fg="#475569").pack(pady=(0, 8))

window.mainloop()

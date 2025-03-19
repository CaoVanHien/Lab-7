import requests
import json
def get_weather(city, api_key):
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']  
        temperature = data['main']['temp']           
        humidity = data['main']['humidity']          
        pressure = data['main']['pressure']          
        
        print(f"weather in {city}:")
        print(f"weather: {weather}")
        print(f"temperature: {temperature}°C")
        print(f"humidity: {humidity}%")
        print(f"pressure: {pressure} hPa \n\n")
    else:
        print(f"Error Unable to get weather data for {city}")


api_key = "2f1dfd1adf9a79b3ab986d14e540fa8c"  
city = "Tokyo"
get_weather(city, api_key)



def get_character_info(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        name = data['name']              
        status = data['status']          
        species = data['species']        
        gender = data['gender']          
        origin = data['origin']['name']  
        location = data['location']['name']  
        image = data['image']            
        
        print("Thông tin nhân vật:")
        print(f"name: {name}")
        print(f"status: {status}")
        print(f"species: {species}")
        print(f"gender: {gender}")
        print(f"origin: {origin}")
        print(f"location: {location}")
        print(f"URL photo: {image}\n\n")
    else:
        print(f"Error: Unable to get character data with ID {character_id}")

character_id = 22  
get_character_info(character_id)

import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

def get_fox_image():
    url = "https://randomfox.ca/floof/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['image']
    return None

def load_image(url):
    response = requests.get(url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    return img

def display_image():
    image_url = get_fox_image()
    if image_url:
        img = load_image(image_url)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo  
    else:
        print("Không thể tải hình ảnh")


root = tk.Tk()
root.title("Generator Hình Ảnh Cáo Ngẫu Nhiên")

label = tk.Label(root)
label.pack()

button = tk.Button(root, text="continue", command=display_image)
button.pack()

display_image()

root.mainloop()
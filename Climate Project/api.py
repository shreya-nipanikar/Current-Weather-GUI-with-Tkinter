from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import requests
import json 


#To exit
def exitt():
    root.quit()
    root.destroy()
    exit() 
    
root = tk.Tk()
root.geometry("800x800")

root.title("My Weather Project Honey!")

welcome_frame = tk.Label(root, text="Welcome!")
welcome_frame.grid(column=0,row=0,padx=8, pady=8,sticky='e')

#api http://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10


#api = json.loads(api_requests.content)

def get_weather():
    #api_key = "d0e66d43dff074870fa0108373244b2a"
  
    # base_url variable to store url 
    #base_url = "http://api.openweathermap.org/data/2.5/weather?"
  
  
    # take a city name from city_field entry box 
    city_name = city_field.get() 
  
    # complete_url variable to store complete url address 
    #complete_url = base_url + "appid =" + api_key + "&q =" + city_name 
  
    # get method of requests module 
    # return response object 
    #response = requests.get(complete_url) 
  
    # json method of response object convert 
    # json format data into python format data 
    #x = response.json() 
  
    api_requests = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=d0e66d43dff074870fa0108373244b2a").json()
    if api_requests["cod"] != "404" : 
        y = api_requests["main"]["temp"]
        temperature_field.insert(15,str(y)+"Kelvin")
    else:
        messagebox.showerror("Error!","City not found. Please enter a valid city")
        


City_label = tk.Label(root,text="City Name: ")
City_label.grid(column=0,row=2,sticky='W')
Temperature_Label = tk.Label(root, text="Temperature: ")
Temperature_Label.grid(column=0,row=3,sticky='W')

city_field = tk.Entry(root)
city_field.grid(column=1,row=2,sticky='W')
temperature_field = tk.Entry(root)
temperature_field.grid(column=1,row=3,sticky='W')

button1 = tk.Button(root,text ="Get temperature!",command = get_weather)
button1.grid(row=4,column=3)


root.mainloop()
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 
import requests, base64
import PIL.ImageTk
import PIL.Image
from urllib.request import urlopen
from tkinter import *
from idlelib.idle_test.test_configdialog import root



#To exit
def exitt():
    root.quit()
    root.destroy()
    exit() 
    
root = tk.Tk()
root.geometry("800x800")

root.title("My Weather Project Honey!")

welcome_frame = ttk.Label(root, text="Welcome!")
welcome_frame.grid(column=0,row=0,padx=8, pady=8,sticky='e')

#Tab
tabcontrol = ttk.Notebook(root)

tab1 = ttk.Frame(tabcontrol)
tabcontrol.add(tab1, text = 'Tab 1')

tab2 = ttk.Frame(tabcontrol)
tabcontrol.add(tab2, text ='Tab 2')

tabcontrol.grid(column = 0, row=10,sticky='W')

#LabelFrame
weather_cities = ttk.Labelframe(tab1, text= "Latest Observations")
weather_cities.grid(column=8,row=8, padx=8, pady=4)

#Label
ttk.Label(weather_cities,text="Location: ").grid(column=6,row=0,sticky='W')

#Combobox
city = tk.StringVar()
cityselected = ttk.Combobox(weather_cities, width = 21, textvariable = city)
cityselected['values'] = ('New York', 'texas','washinton dc', 'florida')
cityselected.grid(column = 7,row=0,padx=1,pady=4)
cityselected.current(0)

max_width = max([len(x)for x in cityselected['values']])
new_width = max_width
cityselected.config(width = new_width)

#Labels
entry_width = max_width + 7
 
ttk.Label(weather_cities, text="Last Updated: ").grid(column=5,row=2,padx=18, pady=14,sticky='W')
updated = tk.StringVar()
updatedEntry = ttk.Entry(weather_cities,width = entry_width,textvariable = updated, state ='writeonly')
updatedEntry.grid(column=7,row=2,sticky='W')

ttk.Label(weather_cities, text="Temperature: ").grid(column=5,row=3,padx=18,pady=14,sticky='W')
temperature = tk.StringVar()
temperature_entry = ttk.Entry(weather_cities,width = entry_width,textvariable = temperature,state='writeonly')
temperature_entry.grid(column=7,row=3,sticky='W')

ttk.Label(weather_cities, text="Weather: ").grid(column=5,row=4,padx=18, pady=14,sticky='W')
weather_updated = tk.StringVar()
weather_update = ttk.Entry(weather_cities,width = entry_width,textvariable = weather_updated, state ='writeonly')
weather_update.grid(column=7,row=4,sticky='W')

ttk.Label(weather_cities, text="Temperature feels like: ").grid(column=5,row=5,padx=18,pady=14,sticky='W')
temp = tk.StringVar()
temp_entry = ttk.Entry(weather_cities,width = entry_width,textvariable = temp,state='writeonly')
temp_entry.grid(column=7,row=5,sticky='W')

ttk.Label(weather_cities, text="Wind: ").grid(column=5,row=6,padx=18, pady=14,sticky='W')
rain_updated = tk.StringVar()
rain_update = ttk.Entry(weather_cities,width = entry_width,textvariable = rain_updated, state ='writeonly')
rain_update.grid(column=7,row=6,sticky='W')

ttk.Label(weather_cities, text="Country: ").grid(column=5,row=7,padx=18,pady=14,sticky='W')
snow_updated = tk.StringVar()
snow_entry = ttk.Entry(weather_cities,width = entry_width,textvariable = snow_updated,state='writeonly')
snow_entry.grid(column=7,row=7,sticky='W')

ttk.Label(weather_cities, text="TimeZone: ").grid(column=5,row=8,padx=18, pady=14,sticky='W')
timezone_updated = tk.StringVar()
timezone_update = ttk.Entry(weather_cities,width = entry_width,textvariable = timezone_updated, state ='writeonly')
timezone_update.grid(column=7,row=8,sticky='W')

ttk.Label(weather_cities, text="Humidity: ").grid(column=5,row=9,padx=18,pady=14,sticky='W')
humidity_updated = tk.StringVar()
humidity_update = ttk.Entry(weather_cities,width = entry_width,textvariable = humidity_updated,state='writeonly')
humidity_update.grid(column=7,row=9,sticky='W')



def get_weather():
    city_name = cityselected.get()
    api_requests = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=d0e66d43dff074870fa0108373244b2a").json()
    
    if api_requests["cod"] != "404" : 
        last_updated = api_requests["sys"]["sunrise"]
        updatedEntry.insert(15,str(last_updated))
        
        temperature_updated = api_requests["main"]["temp"]
        temperature_celsius =int((float(temperature_updated) - 273.15))
        temperature_entry.insert(10,str(temperature_celsius) +"Celsius")
       
        
        current_weather = api_requests["weather"][0]["main"]
        weather_update.insert(15,str(current_weather))
        
        feels_like_temp = api_requests["main"]["feels_like"]
        temperature_feels = int((float(feels_like_temp) - 273.15))
        temp_entry.insert(10,str(temperature_feels) + "Celsius")
        
        wind_current = api_requests["wind"]["speed"]
        rain_update.insert(15,str(wind_current) + "m/hr")
        
        country_current = api_requests["sys"]["country"]
        snow_entry.insert(10,str(country_current))
        
        pressure_current = api_requests["timezone"]
        timezone_update.insert(15,str(pressure_current))
        
        humidity_current = api_requests["main"]["humidity"]
        humidity_update.insert(10,str(humidity_current)+"%")
        
        weather_image = api_requests["weather"][0]["icon"]
        
        print(weather_image)
        
        url_icon = "http://openweathermap.org/img/w/{}.png".format(weather_image)
        ico = urlopen(url_icon)
        open_im = PIL.Image.open(ico)
        open_photo = PIL.ImageTk.PhotoImage(open_im)
        ttk.Label(weather_cities, image=open_photo).grid(column=0, row=1) 
        root.update()
        root.mainloop(0)
          
             
    else:
        messagebox.showerror("Error!","City not found. Please enter a valid city")
    
    
get_weather_button = ttk.Button(weather_cities,text = 'Get Weather!',command= get_weather)
get_weather_button.grid(column = 10,row=0,padx=1,pady=4)




 
 
def clear_all():
    cityselected.delete(0, 'end')
    updatedEntry.delete(0, 'end')
    temperature_entry.delete(0, 'end')
    weather_update.delete(0, 'end')
    temp_entry.delete(0, 'end')
    rain_update.delete(0,'end')
    snow_entry.delete(0,'end')
    timezone_update.delete(0,'end')
    humidity_update.delete(0,'end')
    
    cityselected.focus_set()
    
clear_button = ttk.Button(weather_cities,text= 'Clear All',command= clear_all)
clear_button.grid(column=10, row = 11, padx=1, pady=4)
     
root.mainloop()
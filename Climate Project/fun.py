
import tkinter as tk
from tkinter import Menu 
from tkinter import ttk 


#To exit
def exitt():
    win.quit()
    win.destroy()
    exit() 

win = tk.Tk()

win.title("My Project!")

menuBar = Menu()
win.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = exitt)
menuBar.add_cascade(label="File", menu=fileMenu)

helpMenu = Menu(menuBar, tearoff = 0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help",menu= helpMenu)

editMenu = Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="Edit",menu = editMenu)
editMenu.add_command(label="Undo")
editMenu.add_separator()
editMenu.add_command(label="Copy")
editMenu.add_separator()
editMenu.add_command(label="Paste")
editMenu.add_separator()
editMenu.add_command(label="Cut")

tabControl = ttk.Notebook(win)

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text = 'Tab 1')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text = 'Tab 2')

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text = 'Tab 3')

tabControl.pack(expand = 1, fill = "both")


butn = tk.Button(win, text ="Take it easy!")
butn.pack()

# Creation of new labelframe
weather_cities_frame = ttk.Labelframe(tab1 , text = 'Latest Observation for')
weather_cities_frame.grid(column=0,row=0, padx=8, pady=4)
ttk.Label(weather_cities_frame,text="Location: ").grid(column=0,row=0,sticky='W')


weather_frame = ttk.Labelframe(tab1, text = 'Current weather conditions')
weather_frame.grid(column=0, row=1, padx=55, pady=35)
#ttk.Label(weather_frame, text="Location: ").grid(column=0, row=1, sticky= 'E')

Effected_Areas_frame = ttk.Labelframe(tab2, text = 'Areas Effected Worstest')
Effected_Areas_frame.grid(column = 0, row=0, padx=18, pady=14)
ttk.Label(Effected_Areas_frame, text="States").grid(column=10,row=8, sticky = 'S')

Better_Areas_frame = ttk.Labelframe(tab3, text='Better Conditions')
Better_Areas_frame.grid(column=8 , row=9, padx= 14, pady= 14)
ttk.Label(Better_Areas_frame, text="States").grid(column=0,row=0,sticky = 'W' )


#Creation of combobox
city = tk.StringVar()
cityselected = ttk.Combobox(weather_cities_frame, width =21, textvariable = city)
cityselected['values'] = ('New York', 'Staten Island','Canada', 'florida')
cityselected.grid(column = 1,row=0,padx=14,pady=14)
cityselected.current(0)

max_width = max([len(x)for x in cityselected['values']])
new_width = max_width
cityselected.config(width = new_width)

#labels
entry_width = max_width + 7

ttk.Label(weather_frame, text="Last Updated: ").grid(column=0,row=4,padx=18, pady=14,sticky='W')
updated = tk.StringVar()
updatedentry = ttk.Entry(weather_frame, width = entry_width, textvariable = updated, state='writeonly')
updatedentry.grid(column = 1, row = 4,sticky='W')

ttk.Label(weather_frame, text="Today's Weather: ").grid(column=0,row=6,padx=18, pady=14,sticky='W')
weather = tk.StringVar()
weatherentry = ttk.Entry(weather_frame,width = entry_width, textvariable = weather, state='writeonly')
weatherentry.grid(column = 1,row=6, sticky='W')

ttk.Label(weather_frame, text="Temperature: ").grid(column=0,row=8,padx=18, pady=14,sticky='W')
temperature = tk.StringVar()
temperatureentry = ttk.Entry(weather_frame,width= entry_width, textvariable= temperature,state='writeonly')
temperatureentry.grid(column=1,row=8,sticky='W')

ttk.Label(weather_frame, text="Humidity: ").grid(column=0,row=10,padx=18, pady=14,sticky='W')
humidity = tk.StringVar()
humidityentry = ttk.Entry(weather_frame,width=entry_width,textvariable = humidity, state='writeonly')
humidityentry.grid(column=1,row=10,sticky='W')

ttk.Label(weather_frame, text="Wind: ").grid(column=0,row=12,padx=18, pady=14,sticky='W')
windd = tk.StringVar()
windentry = ttk.Entry(weather_frame,width= entry_width, textvariable= windd,state='writeonly')
windentry.grid(column=1,row=12,sticky='W')

ttk.Label(weather_frame, text="Visibilty: ").grid(column=0,row=14,padx=18, pady=14,sticky='W')
visibile = tk.StringVar()
visibleentry = ttk.Entry(weather_frame,width=entry_width,textvariable = visibile, state='writeonly')
visibleentry.grid(column=1,row=14,sticky='W')

get_weather = ttk.Button(weather_cities_frame,text='Get Weather').grid(column=2, row=0)
#To create space. My most fav part
for x in weather_cities_frame.winfo_children():
    x.grid_configure(padx=15,pady=20)
    
for y in weather_frame.winfo_children():
    y.grid_configure(padx=15,pady=20)
    
# To populate the gui by data
weather_data = {
 'observation_time': '',
 'weather': '',
 'temp_f': '',
 'temp_c': '',
 'relative_humidity': '',
 'wind_string': '',
 'visibility_mi': '',
 }

import urllib.request



win.mainloop()




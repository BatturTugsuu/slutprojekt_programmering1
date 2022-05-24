from os import link
import requests,json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
#om du vill kolla hela json output from den här request kopiera den här linken och klistra in i webbläsaren och sök : https://api.openweathermap.org/data/2.5/weather?appid=af9726a0d34381fc92a3c86967e28656&q=huddinge&units=metric
api_key = "[write your own api key]"
def proceed():
    city=cit.get()
    if city=='':
        return messagebox.showerror('Error','Enter City Name')
    else:
        link = "http://api.openweathermap.org/data/2.5/weather?"
        cityname = city
        query = link + "appid=" + api_key + "&q=" + cityname + "&units=metric"
        response = requests.get(query) 
        data = response.json()  
        if data["cod"] != "404": #om det är inte cod: 404 så kör det här if-satsen, man får cod 200 om det är successivt request i json 
            main = data["main"] 
            currenttemp = main["temp"] 
            currenthumidiy = main["humidity"]
            currentsituation = data["weather"] 
            weather_description = currentsituation[0]["main"]  
            Label(home,text='Temperature: '+str(round(currenttemp))+' °C').place(x=2,y=60)
            Label(home,text='Humidity: '+str(currenthumidiy)).place(x=2,y=90)
            Label(home,text='Description: '+str(weather_description)).place(x=2,y=120)
        else: 
            return messagebox.showerror('Error','No City Found')   
home=Tk()
home.geometry('250x150')
cit=StringVar()
Label(home,text='Weather').grid(row=1,column=2)
Label(home,text='Enter City:').grid(row=2,column=1)
Entry(home,width=15,textvariable=cit).grid(row=2,column=2)
Button(home,text='Proceed',command=proceed).grid(row=2,column=3)
home.mainloop()

from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests, json
import pytz

root=Tk()
root.title("สภาพอากาศ")
root.geometry("800x500+300+200")
root.resizable(False,False)

def getWeather():
    try:    
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExercises")
        location= geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%m %p")
        clock.config(text=current_time)
        name.config(text="เวลาปัจจุบัน")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=01b677fae70272273db401c4a0e6e1bb"

        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']


        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","ความรู้สึก",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("ผิดพลาด","คุณใส่ชื่อประเทศผิด กรุณาใส่ใหม่อีกครั้ง")

#search
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=180,y=20)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=230,y=40)
textfield.focus()

Search_icon=PhotoImage(file="search_icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=540,y=34)


#logo
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=270,y=100)


#buttom
Frame_image=PhotoImage(file="box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",20,"bold"))
name.place(x=30,y=150)
clock=Label(root,font=("Helvetica",30,"bold"),fg="#32CD32")
clock.place(x=60,y=200)

#label
label1=Label(root,text="ลม",font=("Helvetica",20,'bold'),fg="white",bg="#1ab5ef")
label1.place(x=100,y=400)

label2=Label(root,text="ความชื้น",font=("Helvetica",20,'bold'),fg="white",bg="#1ab5ef")
label2.place(x=230,y=400)

label3=Label(root,text="คำอธิบาย",font=("Helvetica",20,'bold'),fg="white",bg="#1ab5ef")
label3.place(x=410,y=400)

label4=Label(root,text="ความดัน",font=("Helvetica",20,'bold'),fg="white",bg="#1ab5ef")
label4.place(x=630,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=550,y=150)
c=Label(font=("arial",15,'bold'))
c.place(x=550,y=250)

w=Label(text=" ",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=100,y=440)
h=Label(text=" ",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=230,y=440)
d=Label(text=" ",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=380,y=440)
p=Label(text=" ",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=630,y=440)


root.mainloop()
from tkinter import *
from PIL import Image,ImageTk
import requests
import json
#ref for api return data
# dum ={"coord":{"lon":79.75,"lat":11.75},
# "weather":[{"id":802,"main":"Clouds","description":"scattered clouds","icon":"03d"}],
# "base":"stations",
# "main":{"temp":301.19,"feels_like":301.91,"temp_min":301.19,"temp_max":301.19,"pressure":1011,"humidity":71,"sea_level":1011,"grnd_level":1010},
# "visibility":10000,
# "wind":{"speed":5.9,"deg":61},
# "clouds":{"all":29},
# "dt":1605858243,
# "sys":{"country":"IN","sunrise":1605832820,"sunset":1605874399},
# "timezone":19800,
# "id":1273802,
# "name":"Cuddalore",
# "cod":200}

root = Tk()
root.title("weather application")
root.geometry("120x70")
root.configure(background="green")


def check_wea():
    global cityn
    cityname=cityn.get()
    try:
        top=Toplevel()
        top.title(cityname+" Weather Report")
        api_request = requests.get('http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=485efa3bf629175ca451e4e32c7f135b'.format(cityname))
        api = json.loads(api_request.content)
        city = api["name"]
        country = api["sys"]["country"]
        weather = api["weather"][0]["main"]
        temp = "Temp : "+str(api["main"]["temp"])
        dis=Label(top,text=country+" - "+city+" - "+weather+" - "+temp,font=("Helvetica",15),background="green")
        dis.pack()
    except Exception as e:
        print(e)
        api = "error..."
        Label(top,text=api,font=("Helvetica",15)).pack()
Label(root,text="Enter a city name :").grid(row=0,column=0)
cityn = Entry(root)
cityn.grid(row=1,column=0)
submit = Button(root,text="Submit",command=check_wea)
submit.grid(row=2,column=0)

# Label(root,text=country).pack()
# Label(root,text=weather).pack()
# Label(root,text=temp).pack()
root.mainloop()
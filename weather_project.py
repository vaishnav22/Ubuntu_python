import requests
from tkinter import *

api_address = 'https://api.openweathermap.org/data/2.5/weather?appid=d0794456a9b267b1569ed57d73d121d9&q='   #api key


######################################################### functon for gettting user input#######################



def getCity():

#city = input("Enter the city: ")

    get_city_user = Entry1.get()


    url = api_address+get_city_user

    jason_data = requests.get(url).json()
    formated_data = jason_data['weather'][0]['main']
    temp = jason_data['main']['temp']
    celsius_temp = temp-273.15
    wind_speed = jason_data['wind']['speed']

    desc = Label(win,text=formated_data)
    desc.grid(row=3)

    temprature = Label(win,text=celsius_temp)
    temprature.grid(row=4)

    wind = Label(win,text=wind_speed)
    wind.grid(row=5)


#print(formated_data)
#print(celsius_temp)
#print(wind_speed)


win = Tk()
win.title('Check Weather')
win.geometry("300x200")


############################################ labels and entry for window ####################
city = Label(win, text = 'City')
city.grid(row=0)

Entry1 = Entry(win)
Entry1.grid(row=0,column=1)

button_1 = Button(win,text = 'Check Weather',command=getCity)
button_1.grid(columnspan=2)

win.mainloop()
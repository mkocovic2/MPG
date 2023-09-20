import tkinter as tk
from tkinter import PhotoImage
import requests

mainWindow = tk.Tk()
mainWindow.title("MPG Calculator")

mainWindow.configure(bg="#f2f2f2")
icon = PhotoImage(file="gaspump.png")
mainWindow.iconphoto(True, icon)
mainWindow.geometry("400x400")
mainWindow.resizable(False, False)


def calculate_mpg():
    try:
        distance = float(distanceInput.get())
        mpg = float(mpgInput.get())
        gas = float(gasInput.get())
        cost = gas * (distance / mpg)
        cost = round(cost, 2)
        resultLabel.config(text="$" + str(cost))
    except ValueError:
        resultLabel.config(text="Invalid input")


def get_mpg():
    try:
        model = modelInput.get()
        api_url = 'https://api.api-ninjas.com/v1/cars?model={}'.format(model)
        response = requests.get(api_url, headers={'X-Api-Key': 'eTiBrxH7G5QF0sDpZMDgZQ==VD7Vt2Oe8aiiZxPd'})
        if response.status_code == requests.codes.ok:
            data = response.json()
            if len(data) > 0:
                vehicle = data[0]
                city_mpg = vehicle['city_mpg']
                highway_mpg = vehicle['highway_mpg']
                apiResult.config(text="City MPG: {}, Highway MPG: {}".format(city_mpg, highway_mpg))
            else:
                apiResult.config(text="Vehicle not found")
        else:
            print("Error:", response.status_code, response.text)
    except:
        apiResult.config(text="API Error")


title = tk.Label(mainWindow, text="MPG Calculator", font=("Arial", 20), bg="#f2f2f2")
title.pack(pady=20)

distanceText = tk.Label(mainWindow, text="Distance to Location:", bg="#f2f2f2")
distanceText.pack()

distanceInput = tk.Entry(mainWindow)
distanceInput.pack()

mpgText = tk.Label(mainWindow, text="MPG:", bg="#f2f2f2")
mpgText.pack()

mpgInput = tk.Entry(mainWindow)
mpgInput.pack()

gasText = tk.Label(mainWindow, text="Gas Price:", bg="#f2f2f2")
gasText.pack()

gasInput = tk.Entry(mainWindow)
gasInput.pack()

submitBtn = tk.Button(mainWindow, text="Calculate", command=calculate_mpg, bg="#4CAF50", fg="white")
submitBtn.pack(pady=20)

resultLabel = tk.Label(mainWindow, text="", font=("Arial", 16), bg="#f2f2f2")
resultLabel.pack()

modelText = tk.Label(mainWindow, text="Find Vehicle MPG:", bg="#f2f2f2")
modelText.pack()

modelInput = tk.Entry(mainWindow)
modelInput.pack()

searchBtn = tk.Button(mainWindow, text="Search", command=get_mpg, bg="#2196F3", fg="white")
searchBtn.pack(pady=10)

apiResult = tk.Label(mainWindow, text="", bg="#f2f2f2")
apiResult.pack()


mainWindow.mainloop()

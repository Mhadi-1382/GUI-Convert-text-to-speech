
# Convert Text To Speech
# Built by Mahdi Rabiee

from tkinter import *
import pyttsx3
import time

# Configure speaking
engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 140)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Function " Run Convert "
def runConvert():
    enterTextConvertGet = enterTextConvert.get()
    enterTextConvertNameGet = enterTextConvertName.get()
    
    engine.save_to_file(enterTextConvertGet, f'{enterTextConvertNameGet}.mp3')
    engine.runAndWait()

    time.sleep(2)

    enterTextConvertGet = enterTextConvert.delete(0, END)
    enterTextConvertNameGet = enterTextConvertName.delete(0, END)

# GUI Convert Text To Speech
root = Tk()

root.title("Convert Text To Speech")
root.geometry("500x300")

root.config(bg='#ffffff')
root.resizable(0,0)


enterTextConvertLabel = Label(root, text='Enter Text To Convert', background='#ffffff')
enterTextConvertLabel.grid(row=0, column=0, padx=(0,340), pady=(0,35), ipady=0)
enterTextConvert = Entry(root, bg='#eeeeee', fg='#000000', width=56, border=1, font='Segoe 11')
enterTextConvert.grid(row=0, column=0, padx=23, pady=(40,10), ipady=10)

enterTextConvertNameLabel = Label(root, text='File Name', background='#ffffff')
enterTextConvertNameLabel.grid(row=1, column=0, padx=(0,400), pady=(0,85), ipady=0)
enterTextConvertName = Entry(root, bg='#eeeeee', fg='#000000', width=56, border=1, font='Segoe 11')
enterTextConvertName.grid(row=1, column=0, padx=23, pady=(30,60), ipady=5)

enterButton = Button(root, bg='#eeeeee', fg='#000000', text='Convert', border=1, width=15, command=runConvert)
enterButton.grid(row=3, column=0, padx=23, pady=(0,0), ipady=8)


root.mainloop()
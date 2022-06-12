import tkinter as tk
import tkinter.font
#import Tkinter.font as tkFont
import RPi.GPIO as GPIO
import time
#from tkinter import *
#import tkinter.font as tkFont
#from guizero import App, Text

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'S': '...',
        'R': '.-.',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}
        
ledPin= 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin,GPIO.OUT)

root = tk.Tk()
myFont = tkinter.font.Font(family = 'Helvetica', size = 18)

def dot():
        GPIO.output(ledPin,1)
        time.sleep(0.2)
        GPIO.output(ledPin,0)
        time.sleep(0.2)

def dash():
        GPIO.output(ledPin,1)
        time.sleep(0.5)
        GPIO.output(ledPin,0)
        time.sleep(0.2)

def exitProgram():
        print("Exit Button pressed")
        GPIO.cleanup()
        root.destroy()

def BlinkMorse():
    inputvalue =morse_code_app.get("1.0","end-1c")
    if (len(inputvalue) < 13):
        for letter in inputvalue: #morse_code_app. value:
           for symbol in CODE[letter.upper()]:
                if symbol == '-':
                        dash()
                elif symbol == '.':
                            dot()
                else:
                        time.sleep(0.5)
        else:
            print("You can only enter 12 characters")
    time.sleep(0.5)
    


morse_code_app =tk.Text(root) 
morse_code_app.pack()

blinktheLED = tk.Button(root, command=BlinkMorse, text="Send")
exButton = tk.Button(root, command = exitProgram, text= "EXIT")
blinktheLED.pack()
exButton.pack()
GPIO.setwarnings(False)
tk.mainloop()
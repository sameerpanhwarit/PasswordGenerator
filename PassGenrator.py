from lib2to3.pygram import Symbols
import numbers
import string
from tkinter import Menu
import sys,os
import random
from time import sleep

def menu():
    print('-'*10,"Strong Password Generator",'-'*10)
    Menu = ['1.Generate Password','2.Exit']
    for i in Menu:
        print(i)
    print('_'*19)
    opt = int(input("Enter Option: "))
    if opt == 1:
        passGen();
    elif opt == 2:
        exit

def passGen():
    os.system('cls')
    print('-'*10,"Password Generator",'-'*10)
    length =int(input("Enter the Length of Password: "))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    allLetters = lower+upper+numbers+symbols
    print(">Generating Password...")
    sleep(0.6)
    temp = random.sample(allLetters,length)
    password="".join(temp)
    print("Your Password is : "+password)
menu();




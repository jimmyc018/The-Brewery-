'''Developed By Jimmy Chan'''

from threading import *
import time, sys
import random
from tkinter import messagebox
import tkinter
from multiprocessing import Process

def TheBrewerySensor():
    messageBoxHide = tkinter.Tk()
    messageBoxHide.withdraw()
    while True:
        beerOneExpectedTemp = random.randint(4,6) 
        beerOneSetTemp = random.randint(4,6)
        print("Beer 1 current temperature: ", beerOneSetTemp)
        if (beerOneExpectedTemp == beerOneSetTemp):
            time.sleep(20)
        elif (beerOneExpectedTemp != beerOneSetTemp):
            time.sleep(20)
            print("Beer 1 temperature is outside the range")
            messagebox.showwarning("Warning","Beer 1 temperature is outside the range")           
        beerTwoExpectedTemp = random.randint(5,6) 
        beerTwoSetTemp = random.randint(5,6)
        print("Beer 2 current temperature: ", beerTwoSetTemp)
        if (beerTwoExpectedTemp == beerTwoSetTemp):
            time.sleep(20)
        elif (beerTwoExpectedTemp != beerTwoSetTemp):
            time.sleep(20)
            print("Beer 2 temperature is outside the range")
            messagebox.showwarning("Warning","Beer 2 temperature is outside the range")
        beerThreeExpectedTemp = random.randint(4,7) 
        beerThreeSetTemp = random.randint(4,7)
        print("Beer 3 current temperature: ", beerThreeSetTemp)
        if (beerThreeExpectedTemp == beerThreeSetTemp):
            time.sleep(20)
        elif (beerThreeExpectedTemp != beerThreeSetTemp):
            time.sleep(20)
            print("Beer 3 temperature is outside the range ")
            messagebox.showwarning("Warning","Beer 3 temperature is outside the range")
        beerFourExpectedTemp = random.randint(6,8) 
        beerFourSetTemp = random.randint(6,8)
        print("Beer 4 current temperature: ", beerFourSetTemp)
        if (beerFourExpectedTemp == beerFourSetTemp):
            time.sleep(20)
        elif (beerFourExpectedTemp != beerFourSetTemp):
            time.sleep(20)
            print("Beer 4 temperature is outside the range")
            messagebox.showwarning("Warning","Beer 4 temperature is outside the range")
        beerFiveExpectedTemp = random.randint(3,5) 
        beerFiveSetTemp = random.randint(3,5)
        print("Beer 5 current temperature: ", beerFiveSetTemp)
        if (beerFiveExpectedTemp == beerFiveSetTemp):
            time.sleep(20)
        elif (beerFiveExpectedTemp != beerFiveSetTemp):
            time.sleep(20)
            print("Beer 5 temperature is outside the range")
            messagebox.showwarning("Warning","Beer 5 temperature is outside the range")
        time.sleep(20)
           
if __name__ == '__main__':
    print("The Brewery - Transport Refrigeration Sensors")
    print("Starting Transport Regfrigeration Sensor .....")
    Thread(target = TheBrewerySensor()).start()
    print("Destination Arrived")
    print("Stopping Transport Regfrigeration Sensor .....")



# GUESS

import random as rnd
import time
number = rnd.randint(1,100)

def intro():
    print("Hi, welcome to the GUESS." + "\n" + "\n")
    time.sleep(1)
    print("In this program, the computer will determine a number between 1 and 100, and you will try to find it."+ "\n" + "\n")
    time.sleep(2)
    print("Ready?"+ "\n")
    time.sleep(1.5)
    print("3"+ "\n")
    time.sleep(1)
    print("2"+ "\n")
    time.sleep(1)
    print("1"+ "\n")
    time.sleep(1)
    print("GO!"+ "\n")


def game(number):
    guess = int(input("GUESS: "+ "\n"+ "\n"))
    counter = 0
    while True:
        if guess != number:
            if guess < number:
                print("\n"+"Up!"+ "\n"+ "\n")
                counter += 1
                time.sleep(0.5)
                guess = int(input("GUESS: "+ "\n"+ "\n"))
            if guess > number:
                print("\n"+"Down!"+ "\n"+ "\n")
                counter += 1
                time.sleep(0.5)
                guess = int(input("GUESS: "+ "\n"+ "\n"))
            if guess != number:
                if counter == 4:
                    print("\n"+"FAIL :D"+ "\n")
                    print("\n"+ "Number: ", number)
                    break
        else:
            print("\n"+"Congratulations!")
            break
intro()
game(number)

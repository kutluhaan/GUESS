
# GUESS

import random as rnd
import time
number = rnd.randint(1,100)

def intro():
    print("Merhaba, GUESS'e hoşgeldiniz." + "\n" + "\n")
    time.sleep(1)
    print("Bu programda bilgisayar 1 ile 100 arasında bir sayı belirleyecek, siz ise bulmaya çalışacaksınız."+ "\n" + "\n")
    time.sleep(2)
    print("Hazır mısın?"+ "\n")
    time.sleep(1.5)
    print("3"+ "\n")
    time.sleep(1)
    print("2"+ "\n")
    time.sleep(1)
    print("1"+ "\n")
    time.sleep(1)
    print("Başla!"+ "\n")


def oyun(number):
    tahmin = int(input("Tahmininizi girin: "+ "\n"+ "\n"))
    sayaç = 0
    while True:
        if tahmin != number:
            if tahmin < number:
                print("\n"+"Yukarı!"+ "\n"+ "\n")
                sayaç += 1
                time.sleep(0.5)
                tahmin = int(input("Tahmininizi girin: "+ "\n"+ "\n"))
            if tahmin > number:
                print("\n"+"Aşağı!"+ "\n"+ "\n")
                sayaç += 1
                time.sleep(0.5)
                tahmin = int(input("Tahmininizi girin: "+ "\n"+ "\n"))
            if tahmin != number:
                if sayaç == 4:
                    print("\n"+"Bulamadın :D"+ "\n")
                    print("\n"+ "Sayı: ", number)
                    break
        else:
            print("\n"+"Tebrikler, bildiniz!")
            break
intro()
oyun(number)
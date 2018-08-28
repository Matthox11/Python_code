#coding:utf-8
import os
def quitter():
    i = 0
    quitter = str()
    while i < 10:
        if quitter.upper() == "Q":
            print("Vous quittez le programme.")
            break
        else:
            quitter = input("Tapez q pour quittter : ")
            os.system("cls")
if __name__ == "__main__":
    quitter()
os.system("pause")

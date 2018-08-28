# coding:utf-8
import os
def verrifConexion(username, passworld):
    usernameInput = input("Quel est votre pseudo ?")
    passworldInput = input("Quel est votre mot de passe ?")
    try:
        if username == usernameInput and passworld == passworldInput:
            print("Mot de passe correct, bienvenue", username)
        else: 
            print("Mot de passe ou pseudo incorrect.Veuillez réessayer")
    except:
        print("Veuillez réessayer")         
if __name__ == "__main__":
    verrifConexion("Matthieu", "mfe2305")
os.system("pause")

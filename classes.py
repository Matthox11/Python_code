#coding:utf-8
import os
class User:

    def __init__(self, nom, age):
        print("Création d'un nouvel utilisateur !")
        self.nom = nom
        self.age = age
    def init(self):
        print("{} {} ans.".format(self.nom, self.age))    
user1 = User("Matthox", 15)
user1.init()
user2 = User("Romain", 13)
user2.init()

os.system("pause")

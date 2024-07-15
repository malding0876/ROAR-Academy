import os

path = os.path.dirname(os.path.abspath(__file__))

file = open(path + '/' + "motto.txt", "w")
file.write("manducare et dormire tota die")
file.close()
file = open(path + "/" + "motto.txt", "r")
print(file.read())
file.close()
file = open(path + "/motto.txt", "a")
file.write("\neat and sleep all day")
file.close()
file = open(path + "/motto.txt", "r")
print(file.read())
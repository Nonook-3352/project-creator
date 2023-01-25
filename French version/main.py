import os


pathactiv = True


files2 = open("data.txt", "r")
test1 = files2.read()
files2.close()

if test1 == "":

    files = open("data.txt", "w")
    inpUSERn = str(input("Quel est votre nom d'utilisateur Windows : "))
    files.write(str(inpUSERn))
    pathC = "C:\\Users\\" + str(inpUSERn)
    files.close()

if test1 != "":
    files3 = open("data.txt", "r")
    test2 = files3.read()
    pathC = test2
    print("Bienvenue, " + test2 + "\n")


print("différents endroits : \n 1 : Bureau \n 2 : Documents \n 3: Dans un Dossier special\n ")

inpUSER = str(input("dans quelle endroit voulez vous crée le projet(donner le numéro) : "))

if inpUSER == "1":
    pathC = "C:\\Users\\" + str(test2) + "\\Desktop"

if inpUSER == "2":
    pathC = "C:\\Users\\" + str(test2) + "\\Documents"

if inpUSER == "3":
    inpUSERp = str(input("Entrer le chemin d'accès : "))
    os.chdir(inpUSERp)
    pathactiv = False

if pathactiv == True:
    os.chdir(pathC)

inpUSERN = input("Entrez le nom de votre projet : ")


print("type de projet : \n 1 : HTML")

inpUSERx = str(input("quels type de projet voulez vous crée (entrer le numéro) : "))


if inpUSERx == "1":
    os.mkdir(str(inpUSERN))
    os.chdir(pathC + "\\" + str(inpUSERN))
    os.mkdir('img')
    myFile = open("index.html", "w+")
    myFile.close()
    myFile2 = open("styles.css", "w+")
    myFile2.close()

htmlstart = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
   
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>webpage</title>
    
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
</body>
</html>"""

files4 = open("index.html", "w")
files4.write(htmlstart)
files4.close()







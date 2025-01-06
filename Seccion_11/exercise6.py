with open("../files/bear2.txt", "r") as file:
    content = file.read()


with open("../files/bear1.txt", "a") as myfile:
    myfile.write(content)
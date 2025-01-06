with open("../files/vegetables.txt","a+") as file:
    file.write("\nGarlic")
    file.seek(0)
    content = file.read()
    

print(content)
with open("../files/bear.txt","r") as file:
    content = file.read()
    
with open("../files/first.txt","w") as myfile:
    
    myfile.write(content[:90])
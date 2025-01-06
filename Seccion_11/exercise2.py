def readfiles(character,pathname):
    file = open(pathname)
    content = file.read()
    return content.count(character)


print(readfiles("b","../files/bear.txt"))
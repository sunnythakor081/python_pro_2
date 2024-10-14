def WriteFile(fileName,content):
    file = open("Unit - 2/08Program/"+fileName,"w")
    file.write(content)
    file.close()


def ReadFile(fileName):
    file = open("Unit - 2/08Program/"+fileName,"r")
    content = file.read()
    print(content)


def copyFile(fileName,destinationFileName):
    file = open("Unit - 2/08Program/"+fileName,"r")
    content= file.read()

    copyfile = open("Unit - 2/08Program/"+destinationFileName,"w")
    copyfile.write(content)

    file.close()
    copyfile.close()


fileName = input("Enter a File Name : ")
content = input("Enter a content Which you wann to insert : ")

WriteFile(fileName,content)
ReadFile(fileName)

fileName = input("Enter Old File Name : ")
destinationFileName = input("Enter a New File Name to copy : ")
copyFile(fileName,destinationFileName)
ReadFile(destinationFileName)
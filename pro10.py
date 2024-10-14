#  Write a programme to Find and Replace all the occurrences of a word ‘gujarat’ in a file with ‘gujrat’. 

def process(fileName,newFileName,oldWord,newWord):
    file = open("Unit - 2/10Program/"+fileName,"r")
    content = file.read()
    file.close()

    # print(content)
    newContent = content.replace(oldWord,newWord)
    # print(newContent)

    file = open('Unit - 2/10Program/'+newFileName,"w")
    file.write(newContent)
    file.close()

    print(f"{oldWord} is replaced with the {newWord}")



process("file.txt","file1.txt","Gujarat","Gujrat")
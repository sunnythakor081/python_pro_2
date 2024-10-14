def textSpliter(content):
    """Split the given text to the word"""
    return content.split()

def generateSentence(words):
    """Generate sentance is used for join all the words"""
    sentence = []
    for word in words:
        sentence.append(word)

    sentences = ' '.join(sentence)
    return sentences



def process(fileName,destinatioFileName):
    file = open("Unit - 2/09Program/"+fileName,"r")
    content = file.read()
    file.close()

    words = textSpliter(content)
    
    sentence = generateSentence(words)
    
    file = open("Unit - 2/09Program/"+destinatioFileName,"w")
    file.write(sentence)
    file.close()

    print(f"Processed text has been written to {destinatioFileName}. ")


process('file.txt','file1.txt')
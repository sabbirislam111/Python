

def reverseWordSentence(Sentence):
    words = Sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence
 

Sentence = "Programming Hero is the best"
print(reverseWordSentence(Sentence))
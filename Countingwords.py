cw = input("Enter text: ")
characterCount = 0
wordCount = 1

for i in cw:
    characterCount = characterCount +1
    
if (i == ''):
        wordCount = wordCount + 1

print ("No.of words in the text: ")
print (wordCount)

print ("number of characters in the text: ")
print (characterCount)
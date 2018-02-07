# Writing to Files

text = 'Sample text to save\nNew line!'

saveFile = open('exampleFile.txt','w')

saveFile.write(text)
saveFile.close()

# Appending Files

appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
appendFile.close()


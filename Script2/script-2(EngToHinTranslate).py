#author: Dhrumil Mevada
#This code will read panish text from file and translate(convert) to english text and write in a new file 
from googletrans import Translator

with open('spanish_text.txt') as f:
    text_to_translate = f.read()
    translator = Translator()
    # print(translator.detect(text_to_translate))
    result = translator.translate(text_to_translate,dest='en').text
with open('translated_spanish_text_into_english.txt','w') as f:
    f.write(result)
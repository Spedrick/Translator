from googletrans import Translator
text = input('Enter your text:- ')

# Creating an instance of Translator to use
# Google Translate ajax API
translator = Translator()

# detect- auto detects language of the input text
dt = translator.detect(text)
print(dt)

# translate()-translates the text from source language to destination language
# translate(self, text, dest='en', src='auto', **kwargs)
# if we don't specify the dest(destination language) then
# it translates to english
translated = translator.translate(text)

print(translated.text)

#Import the libraries
from newspaper import Article
import nltk
from gtts import gTTS
import os

#Get the article
article = Article('https://byjus.com/free-ias-prep/important-articles-in-constitution-india/#:~:text=There%20are%20448%20articles%20in,%2C%20Fundamental%20Rights%2C%20and%20more.')

article.download()
article.parse() # parse function splits the source code into tokens based on the grammar

nltk.download('punkt') #This tokenizer divides a text into a list of sentences
article.nlp()

#Get the articles text
mytext = article.text

language = 'en' #English

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save("read_article.mp3")
os.system("start read_article.mp3")
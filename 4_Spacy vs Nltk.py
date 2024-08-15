'''
Firstly spacy is OOP liberary                    pip install spacy then python -m spacy download en
And NLTK is string processing liberary           pip install nltk thne nltk.download('punkt')
'''
import spacy

nlp = spacy.load("en_core_web_sm")              # english token

doc = nlp('Dr. sumit want ot know your details. Mr.Rohit we hace to meet them')


for sentence in doc.sents:               # Sentence tokenizing
    print(sentence)

for sentence in doc.sents:               # Sentence tokenizing
  for word in sentence:                  # split the word        word tokenizing
    print(word,end= ' | ')



    
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
nltk.download('punkt')


print(sent_tokenize('Dr. sumit want ot know your details. Mr.Rohit we hace to meet them'))
print(word_tokenize('Dr. sumit want ot know your details. Mr.Rohit we hace to meet them'))
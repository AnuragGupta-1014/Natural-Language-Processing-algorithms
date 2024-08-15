from nltk.stem import PorterStemmer
stemmer = PorterStemmer()                   # gives the lemma of given words
 
# Firstly stemming that is done by only NLTK
words = ["eating", "eats", "eat", "ate", "adjustable", "rafting", "ability", "meeting"]


# stemming just remove some postfix like - ing,s,able thats why it is not as suitable as lemmaization
for word in words:
    print(word, "|", stemmer.stem(word))

print('-'*90)
# lemmatization
import spacy

nlp = spacy.load('en_core_web_sm')      #sm is small as well as md is midden 


# doc = nlp("Mando talked for 3 hours although talking isn't his thing")
doc = nlp("eating eats eat ate adjustable rafting ability meeting better")
for token in doc:
    print(token, " | ", token.lemma_)

print(nlp.pipe_names)

ar = nlp.get_pipe('attribute_ruler')
ar.add([[{"TEXT":"Bro"}],[{"TEXT":"Brah"}]],{"LEMMA":"Brother"})   # changing some lemma

doc = nlp("Bro, you wanna go? Brah, don't say no! I am exhausted")
for token in doc:
    print(token.text, "|", token.lemma_)
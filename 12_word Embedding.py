# word embedding vector the similiar meaning words like - animal and dog, bread and food
import spacy

# word vectors occupy lot of space. hence en_core_web_sm model do not have them included. 
# run "python -m spacy download en_core_web_lg" to install large english model
nlp = spacy.load("en_core_web_lg")

doc  = nlp('dog is a animal sdndsfsf')

for token in doc:
    print(token.text ,'Vector:', token.has_vector,'OOV:',token.is_oov)  

base_token = nlp("bread")
doc = nlp("breads bread sandwich burger car tiger human wheat")
for token in doc:
    print(f"{token.text} <-> {base_token.text}:", token.similarity(base_token))


def similarity(base_word, words_to_compare):
    base_token = nlp(base_word)
    doc = nlp(words_to_compare)
    for token in doc:
        print(f"{token.text} <-> {base_token.text}: ", token.similarity(base_token))
        
print(similarity("iphone", "apple samsung iphone dog kitten"))
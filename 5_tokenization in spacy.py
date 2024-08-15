import spacy

nlp = spacy.blank('en')
# nlp = spacy.blank('fr')               # franch
# nlp = spacy.blank('hi')               # hindi

doc = nlp('Dr. sumit want ot know your details. Mr.Rohit we hace to meet them')
doc1 = nlp('''let's go to n.y.!''')

for word in doc:
    print(word,end='-')

print()
for word in doc1:
    print(word,end='    ')

# Print the first token
print('\n', doc[0],doc[2:6],doc[-2])  # This should print 'Dr.'


print('word',type(word))
print('nlp',type(nlp))
print(type(doc))


for token in doc:
    print(token, "==>", "index: ", token.i, "is_alpha:", token.is_alpha, 
          "is_punct:", token.is_punct, 
          "like_num:", token.like_num,
          "is_currency:", token.is_currency,
         )

print()
print()
with open('students.txt') as f:
    text = f.readlines()

print(text)
print('-'*56)
txt = " ".join(text)
print(txt)

doc = nlp(txt)
emails = []
for token in doc:
    if token.like_email:
        emails.append(token.text)
print(emails)   

# using hindi API NLP

nlp_hi = spacy.blank('hi')

doc_2 = nlp_hi('हेलो अरेयोन मेरा नाम सन्न है | 400 $ ')

for token in doc_2:
    print(token,'    ', token.is_currency, token.like_num)

# more easier

tokens = [token.text for token in doc_2] 
print(tokens)

# spliting the word 

from spacy.symbols import ORTH


nlp.tokenizer.add_special_case("gimme", [
    {ORTH: "gim"},
    {ORTH: "me"},
])
doc_3 = nlp("gimme double cheese extra large healthy pizza")
tokens = [token.text for token in doc_3]
print(tokens)


text='''
Look for data to help you address the question. Governments are good
sources because data from public research is often freely available. Good
places to start include http://www.data.gov/, and http://www.science.
gov/, and in the United Kingdom, http://data.gov.uk/.
Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, 
and the European Social Survey at http://www.europeansocialsurvey.org/.
'''

urls = nlp(text)

urls = [token.text for token in urls if token.like_url]
print(urls)

transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"
doc = nlp(transactions)
for token in doc:
    if token.like_num and doc[token.i+1].is_currency:
        print(token.text, doc[token.i+1].text)      
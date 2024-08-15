# stop word  part of pre processing
# that is use to remove the common words like = is,are ,the,that,where,what,when
import spacy

from spacy.lang.en.stop_words import STOP_WORDS

print(len(STOP_WORDS))

nlp = spacy.load("en_core_web_sm")
doc = nlp("We just opened our wings, the flying part is coming soon")
for token in doc:
    if token.is_stop:
        print(token)


def preprocess(text):
    doc = nlp(text)
    
    no_stop_words = [token.text for token in doc if not token.is_stop]
    return " ".join(no_stop_words)            

print('-'*90)
print(preprocess("Musk wants time to prepare for a trial over his"))
print('-'*90)


import pandas as pd
df = pd.read_json("doj_press.json",lines=True)
print(df.shape)

df = df[df["topics"].str.len() != 0]
print(df.head())

print('-'*90)

dff = df["contents_new"] = df.contents.apply(preprocess)
print(dff.head())
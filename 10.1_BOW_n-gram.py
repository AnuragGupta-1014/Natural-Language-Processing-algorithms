from sklearn.feature_extraction.text import CountVectorizer

v = CountVectorizer()
v.fit(["Thor Hathodawala is looking for a job"])
print(v.vocabulary_)

print('-'*96)

v = CountVectorizer(ngram_range=(2,2))                   # n-gram -2
v.fit(["Thor Hathodawala is looking for a job"])
print(v.vocabulary_)


import spacy

# load english language model and create nlp object from it
nlp = spacy.load("en_core_web_sm") 

def preprocess(text):
    # remove stop words and lemmatize the text
    doc = nlp(text)
    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)
    
    return " ".join(filtered_tokens) 
print(preprocess("Thor ate pizza"))
print(preprocess("Loki is eating pizza"))
print('-'*96)

corpus = [
    "Thor ate pizza",
    "Loki is tall",
    "Loki is eating pizza"
]

corpus_processed = [
    preprocess(text) for text in corpus
]
print(corpus_processed)

v.fit(corpus_processed)
print(v.vocabulary_)

# now transfrom the str in vector

v.transform(["Thor eat pizza"]).toarray()   


import pandas as pd

df = pd.read_json('news_dataset.json')
print(df.shape)

print(df.category.value_counts())

min_samples = 1381 # we have these many SCIENCE articlesis our minority class
# and making all column of same size as science 

df_business = df[df.category=="BUSINESS"].sample(min_samples, random_state=1014)
df_sports = df[df.category=="SPORTS"].sample(min_samples, random_state=1014)
df_crime = df[df.category=="CRIME"].sample(min_samples, random_state=1014)
df_science = df[df.category=="SCIENCE"].sample(min_samples, random_state=1014)

df_balanced = pd.concat([df_business,df_sports,df_crime,df_science],axis=0)
print(df_balanced.category.value_counts())

df_balanced['category_num'] = df_balanced['category'].map({
    'BUSINESS': 0,
    'SPORTS': 1, 
    'CRIME': 2, 
    'SCIENCE': 3
})               # text to int for model build purpose

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    df_balanced.text,                                             # X
    df_balanced.category_num,                                     # y
    test_size=0.2,
    random_state=1014,
    stratify=df_balanced.category_num                             # use to take equal set of data
)

print(X_train.shape)
print(X_train.head(2))



from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
# create a pipeline object
clf = Pipeline([
     ('vectorizer_bow', CountVectorizer(ngram_range = (1, 1))),        #using the ngram_range parameter 
     ('Multi NB', MultinomialNB())         
])
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))


# n-gram
clf = Pipeline([
    ('vectorizer_1_2_gram', CountVectorizer(ngram_range = (1, 2))),        #using the ngram_range parameter 
     ('Multi NB', MultinomialNB())         
])
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(classification_report(y_test, y_pred))

# we can apply preporcess func for pre processing all the sentence and build the model
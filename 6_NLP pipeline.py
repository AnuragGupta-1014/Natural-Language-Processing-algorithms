
'''                  NLP
Text =>  tokenizer -> tagger|parser|leematizer | ne r|...  =>   doc

'''
import spacy

nlp = spacy.blank("en")                # it just a tokenizer
doc = nlp("Captain america ate 100$ of samosa. Then he said I can do this all day.")

tokens = [token.text for token in doc]
print(tokens)
nlp = spacy.load("en_core_web_sm") # its have all pipeline stuff

print(nlp.pipe_names)


doc = nlp("Captain america ate 100$ of samosa. Then he said I can do this all day.")
for token in doc:
    print(token, " | ", spacy.explain(token.pos_), " | ", token.lemma_)
    # pos_ is poart of speech and lemma gives the base tense form

doc = nlp("Tesla Inc is going to acquire twitter for $45 billion")
for ent in doc.ents:                      # ner
    print(ent.text, ent.label_)

from spacy import displacy

# print(displacy.render(doc, style="ent"))
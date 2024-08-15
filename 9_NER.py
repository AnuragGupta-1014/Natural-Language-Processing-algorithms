# Name Entity Recognition(ner)             tokens in NLP pipeline
import spacy

nlp = spacy.load("en_core_web_sm")
print(nlp.pipe_names)


doc = nlp("Tesla Inc is going to acquire twitter for $45 billion")
for ent in doc.ents:
    print(ent.text, " | ", ent.label_, " | ", spacy.explain(ent.label_))


from spacy import displacy

print(displacy.render(doc, style="ent"))
print('-'*100)
print(nlp.pipe_labels['ner'])

doc = nlp("Michael Bloomberg founded Bloomberg in 1982")
for ent in doc.ents:
    print(ent.text, "|", ent.label_, "|", spacy.explain(ent.label_))
print('-'*100)

doc = nlp("Tesla is going to acquire Twitter for $45 billion")
for ent in doc.ents:
    print(ent.text, " | ", ent.label_)
print('-'*100)

from spacy.tokens import Span

s1 = Span(doc, 0, 1, label="ORG")
s2 = Span(doc, 5, 6, label="ORG")

doc.set_ents([s1, s2], default="unmodified")
for ent in doc.ents:
    print(ent.text, " | ", ent.label_)
import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp("Elon flew to mars yesterday. He carried biryani masala with him")
for token in doc:
    print(token," | ", token.pos_, " | ", spacy.explain(token.pos_))

print('='*90)
doc = nlp("Wow! Dr. Strange made 265 million $ on the very first day")
for token in doc:
    print(token," | ", token.pos_, " | ", spacy.explain(token.pos_))

print('='*90)

doc = nlp("Wow! Dr. Strange made 265 million $ on the very first day")
for token in doc:
    print(token," | ", token.pos_, " | ", spacy.explain(token.pos_), " | ", token.tag_, " | ", spacy.explain(token.tag_))


print('='*90)


earnings_text="""Microsoft Corp. today announced the following results for the quarter ended December 31, 2021, as compared to the corresponding period of last fiscal year:

·         Revenue was $51.7 billion and increased 20%
·         Operating income was $22.2 billion and increased 24%
·         Net income was $18.8 billion and increased 21%
·         Diluted earnings per share was $2.48 and increased 22%
“Digital technology is the most malleable resource at the world’s disposal to overcome constraints and reimagine everyday work and life,” said Satya Nadella, chairman and chief executive officer of Microsoft. “As tech as a percentage of global GDP continues to increase, we are innovating and investing across diverse and growing markets, with a common underlying technology stack and an operating model that reinforces a common strategy, culture, and sense of purpose.”
“Solid commercial execution, represented by strong bookings growth driven by long-term Azure commitments, increased Microsoft Cloud revenue to $22.1 billion, up 32% year over year” said Amy Hood, executive vice president and chief financial officer of Microsoft."""

doc = nlp(earnings_text)
filtered_tokens = []

for token in doc:
    if token.pos_ not in ["SPACE", "PUNCT", "X"]:     # remove this 
        filtered_tokens.append(token)

print(filtered_tokens[:10])
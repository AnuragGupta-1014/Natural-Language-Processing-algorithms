import gensim.downloader as api

wv = api.load('glove-wiki-gigaword-100')

print(wv.similarity(w1="great", w2="good"))

# print(wv.most_similar("good"))
# print(wv.most_similar("cat"))

# print(wv.most_similar(positive=['king', 'woman'], negative=['man'], topn=5))
print(wv.most_similar(positive=['france', 'berlin'], negative=['paris'], topn=5))

print(wv.doesnt_match(["facebook", "cat", "google", "microsoft"]))
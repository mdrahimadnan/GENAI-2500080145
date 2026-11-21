corpus = {"play": 5, "playing": 3, "player": 2}

print("corpus:", corpus)
print("length of corpus:", len(corpus))
for [k,v] in corpus.items():
    print(k)

    for v in corpus.values():
        print(v)
        
    for [k,v] in corpus.items():
        print(k, v)
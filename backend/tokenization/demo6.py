# word level tokenization
text = input("Enter a sentence: ") or "I love programming in Python!"
print("text:", text)
tokens = text.split()
print("tokens:", tokens)
print("length of tokens:", len(tokens))
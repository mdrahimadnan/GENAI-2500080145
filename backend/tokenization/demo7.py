#character level tokenization
text = input("Enter a sentence: ") or "I love programming in Python!"
print("text:", text)
print("Length:", len(text))

characters = list(text)
print("characters in the given text:", characters)
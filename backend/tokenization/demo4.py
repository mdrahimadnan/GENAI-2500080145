word = input("Enter a word: ") or " I love Python"
print("word:", word)
print ("Length of the word", len(word))

characters = list(word)
print("characters in the given word:", characters)


pairs=list(zip(characters,characters[1:]))

print("adjacent character pairs in the given word:", pairs)
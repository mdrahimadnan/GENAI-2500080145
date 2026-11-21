token = ["i","am","under","the","water","and ","i","am","drowning"]
print("tokens:", token)

print("length of tokens:",len(token))
print("first token:",token[0])
print("last token:",token[-1])
print("last token:",token[len(token)-1])

print("first two tokens:",token[0:2])
print("tokens in reverse order:",token[::-1])
print("last two tokens:",token[-2:])
for token in token:      
    print(token, end=", ")
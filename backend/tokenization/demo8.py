#bpe tokenization using pre-trained GPT-2 tokenizer
from transformers import AutoTokenizer

from collections import Counter

tokenizer = AutoTokenizer.from_pretrained("gpt2")

text = input("Enter a sentence: ") or "I love programming in Python!"
tokens = tokenizer.tokenize(text)

print("tokens:", tokens)
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("original sentence:", text)
print("BPE tokens:", tokens)
print("Token IDs:", token_ids)
print("length of tokens:", len(tokens))
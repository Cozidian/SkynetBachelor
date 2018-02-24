#!/usr/bin/env python
# -*- coding: utf-8 -*-
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.text import text_to_word_sequence

t = Tokenizer()
tt = text_to_word_sequence

# data = open('test.txt').readlines()
data = ["Hello this is a text"]

print(data)
# t.fit_on_texts(data)
test = tt(data)
print(test)

# summarize what was learned
# print(t.word_counts)
# print(t.document_count)
# print(t.word_index)
# print(t.word_docs)

# encoded_text = t.texts_to_matrix(t, mode='count')
# encoded_text = t.texts_to_sequences_generator(t)
# print(encoded_text)

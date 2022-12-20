import re
import textstat
import nltk
nltk.download('punkt')

input_file = open('sample.txt', 'r', encoding='utf-8')
text_string = input_file.read().lower()
sentences = nltk.sent_tokenize(text_string)
tokens = nltk.word_tokenize(text_string)

print(sentences)

print(textstat.flesch_reading_ease(text_string))
print(textstat.gunning_fog(text_string))
print(textstat.automated_readability_index(text_string))
print(textstat.flesch_kincaid_grade(text_string))
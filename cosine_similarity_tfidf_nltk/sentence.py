from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize


text="""Hello Mr. Smith, how are you doing today? The weather is great, and city is awesome.
The sky is pinkish-blue. You shouldn't eat cardboard"""
tokenized_text=sent_tokenize(text)
print(tokenized_text)

print("\n")

tokenized_word=word_tokenize(text)
print(tokenized_word)

print("\n")

fdist = FreqDist(tokenized_word)
print(fdist)
print("\n")

stop_words=set(stopwords.words("english"))
print(stop_words)

print("\n")



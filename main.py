# import pandas as pd
import nltk
# import numpy as np
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('omw-1.4')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')

document = 'test.txt'

with open(document, encoding='ISO-8859-2') as f:
    text = f.read()
# with open('kindle.txt', encoding='UTF-8') as f:
#     text = f.read()

sent_tokenizer = PunktSentenceTokenizer(text)
sents = sent_tokenizer.tokenize(text)

print(word_tokenize(text))
print(sent_tokenize(text))

porter_stemmer = PorterStemmer()

nltk_tokens = nltk.word_tokenize(text)

for w in nltk_tokens:
    print("Actual: % s Stem: % s" % (w, porter_stemmer.stem(w)))


wordnet_lemmatizer = WordNetLemmatizer()
nltk_tokens = nltk.word_tokenize(text)

for w in nltk_tokens:
    print("Actual: % s Lemma: % s" % (w, wordnet_lemmatizer.lemmatize(w)))

text = nltk.word_tokenize(text)
print(nltk.pos_tag(text))

# main
sid = SentimentIntensityAnalyzer()
with open(document, encoding='ISO-8859-2') as f:
    print(end='\n\n')
    for text in f.read().split('\n'):
        print(text)
        scores = sid.polarity_scores(text)
        for key in sorted(scores):
            print('{0}:{1} '.format(key, scores[key]), end='')
        print(end='\n\n')

    print()
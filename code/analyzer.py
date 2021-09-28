import pandas as pd
import numpy as np
import re
import Levenshtein as lev
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
  
warnings.filterwarnings(action = 'ignore')
  
import gensim
from gensim.models import Word2Vec

class Analyzer:
	def __init__(self, status_list):
		self.status_list = status_list
		self.X = X 
		self.Y = Y 
		self.sid = SentimentIntensityAnalyzer()

		# Create CBOW model
		self.CBOW = gensim.models.Word2Vec(self.status_list, min_count = 1, 
		                              size = 100, window = 5)

		# Create Skip Gram model
		self.skipgram = gensim.models.Word2Vec(self.status_list, min_count = 1, size = 100,
                                             window = 5, sg = 1)

	def compound_sentiment(self):
		return [self.sid.polarity_scores(x)['compound'] for x in self.status_list]

	def edit_distance(self, astr, bstr):
		return lev.distance(astr, bstr)

	def cosine_similarity_CBOW(self, astr, bstr):
		return self.CBOW.similarity(astr, bstr)

	def cosine_similarity_skipgram(self, astr, bstr):
		return self.skipgram.similarity(astr, bstr)



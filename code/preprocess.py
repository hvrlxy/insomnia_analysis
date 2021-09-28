from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import numpy as np
import re
from nltk.tokenize import TweetTokenizer
from nltk.stem import PorterStemmer
from sklearn.model_selection import train_test_split
from sklearn import svm
import Levenshtein as lev
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Preprocess():
	def __init__(self):
		self.tk = TweetTokenizer()
		self.ps = PorterStemmer()
		self.nlp = spacy.load('en_core_web_sm')
		self.nlp.add_pipe("spacytextblob")

	def get_status_list(self):
		return list(self.tweets_df['status'])

	def preprocess_status(self, status: str):
		status = status.lower()
		url_regex = 'https://[a-zA-Z0-9.,/]*'
		status = re.sub(url_regex, '', status)

		tag_regex = '@[a-zA-Z0-9.,/_]*'
		status = re.sub(tag_regex, '', status)
		status = self.tk.tokenize(status)
		status = [self.ps.stem(text) for text in status]

		new_status = ''
		for w in status:
			new_status += w + ' '
		return new_status

	def preprocess_status_list(self, status_list):
		return [self.preprocess_status(status) for status in status_list]

	def vectorization(self, status_list):
		vectorizer = TfidfVectorizer()
		X = vectorizer.fit_transform(status_list)
		return X, vectorizer

import json
from urllib.request import urlopen
from get_urls import *
import pandas as pd

class Get_DataFrame():
	def __init__(self):
		self.g = Get_URLs()

	def get_submission(self, q=None, size=None, subreddit=None, sort_type='created_utc', after=None, before=None):
		url = self.g.get_url_submission(q=q, size=size, subreddit=subreddit, sort_type=sort_type, after=after, before=before)
		response = urlopen(url)
		data = json.loads(response.read())
		return data

	def get_comment(self, q=None, ids=None, size=None, subreddit=None, sort_type='created_utc', after=None, before=None):
		url = self.g.get_url_comment(q=q, ids=ids, size=size, subreddit=subreddit, sort_type=sort_type, after=after, before=before)
		response = urlopen(url)
		data = json.loads(response.read())
		return data

	def get_submission_df(self, q=None, size=None, subreddit=None, sort_type='created_utc', after=None, before=None):
		submissions = self.get_submission(q=q, size=size, subreddit=subreddit, sort_type=sort_type, after=after, before=before)
		submissions = submissions['data']
		submission_df = pd.DataFrame(columns=['id', 'title', 'selftext', 'subreddit', 'created_utc'])
		for submission in submissions:
			try:
				new_row = [submission['id'], submission['title'], submission['selftext'], submission['subreddit'], submission['created_utc']]
			except Exception as e:
				continue
			a_series = pd.Series(new_row, index = submission_df.columns)
			submission_df = submission_df.append(a_series, ignore_index=True)

		return submission_df

	def get_comment_df(self, q=None, ids=None, size=None, subreddit=None, sort_type='created_utc', after=None, before=None):
		comments = self.get_comment(q=q, ids=ids, size=size, subreddit=subreddit, sort_type=sort_type, after=after, before=before)
		comments = comments['data']
		comment_df = pd.DataFrame(columns=['id', 'body', 'subreddit', 'created_utc'])
		for comment in comments:
			try:
				new_row = [comment['id'], comment['body'], comment['subreddit'], comment['created_utc']]
			except Exception as e:
				continue
			a_series = pd.Series(new_row, index = comment_df.columns)
			comment_df = comment_df.append(a_series, ignore_index=True)

		return comment_df

	def get_comments_by_submission(self, submission_ids):
		url = self.g.get_url_comment_ids(submission_ids=submission_ids)
		response = urlopen(url)
		data = json.loads(response.read())
		return data['data']

	def get_comments_by_submission_df(self, submission_ids):
		comments = self.get_comments_by_submission(submission_ids)
		comment_df = pd.DataFrame(columns=['id', 'body', 'subreddit', 'created_utc'])
		for comment in comments:
			try:
				cmt = self.get_comment(ids=comment)
			except Exception as e:
				continue
			cmt = cmt['data'][0]
			new_row = [cmt['id'], cmt['body'], cmt['subreddit'], cmt['created_utc']]
			a_series = pd.Series(new_row, index = comment_df.columns)
			comment_df = comment_df.append(a_series, ignore_index=True)
		return comment_df

#test code
# pd.set_option("display.max_rows", None, "display.max_columns", None)
# d = Get_DataFrame()
# print(d.get_submission_df(subreddit='insomnia', size='100', before='1632165389'))

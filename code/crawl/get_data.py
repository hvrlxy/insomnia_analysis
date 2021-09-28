import json
from urllib.request import urlopen
from get_urls import *
from get_dataframe import *
import pandas as pd
import time

class Get_Data():
	def __init__(self, num_days):
		self.d = Get_DataFrame()
		self.num_days = num_days
		self.submission_list = []

	def get_all_submissions(self, q=None, size=None, subreddit=None, sort_type='created_utc'):
		submission_df = pd.DataFrame(columns=['id', 'title', 'selftext', 'subreddit', 'created_utc'])
		before_days = '1603287224'
		is_done = False
		count = 0
		while not is_done:
			try:
				sub_df = self.d.get_submission_df(q=q, size=size, subreddit=subreddit, sort_type=sort_type, before=before_days)
			except Exception as e:
				sub_df = pd.DataFrame(columns=['id', 'title', 'selftext', 'subreddit', 'created_utc'])
			count += len(sub_df)
			print(count)
			if len(sub_df) == 0:
				is_done = True
			else:
				submission_df = submission_df.append(sub_df, ignore_index=True)
				before_days = str(sub_df['created_utc'][len(sub_df) - 1])
			time.sleep(3)
		self.submission_list = list(submission_df['id'])
		return submission_df

	def get_all_comments(self, q=None, ids=None, size=None, subreddit=None, sort_type='created_utc'):
		comment_df = pd.DataFrame(columns=['id', 'title', 'selftext', 'subreddit', 'created_utc'])
		before_days = '1632406692'
		is_done = False
		count = 0
		while not is_done and count < 10000:
			try:
				sub_df = self.d.get_comment_df(q=q, size=size, subreddit=subreddit, sort_type=sort_type, before=str(before_days))
			except Exception as e:
				sub_df = pd.DataFrame(columns=['id', 'title', 'selftext', 'subreddit', 'created_utc'])
			print(count)
			if len(sub_df) == 0:
				is_done = True
			else:
				count += len(sub_df)
				comment_df = comment_df.append(sub_df, ignore_index=True)
				before_days = str(sub_df['created_utc'][len(sub_df) - 1])
			time.sleep(3)
		self.comment_list = list(comment_df['id'])
		return comment_df

	# def get_comment_by_submission(self, submission_list=self.submission_list):
	# 	comment_df = pd.DataFrame(columns=['id', 'body', 'subreddit'])
	# 	for ID in submission_list:
	# 		cmt_df = self.d.get_comments_by_submission_df(ID)
	# 		comment_df = comment_df.append(cmt_df, ignore_index=True)
	# 	return comment_df

#test code
p = Get_Data(180)
pd.set_option("display.max_rows", None, "display.max_columns", None)
df = p.get_all_comments(subreddit='insomnia', size='100')
df.to_csv('comment.csv')
print(len(df))

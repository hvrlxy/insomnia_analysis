import pandas as pd

class Get_URLs():
	def get_url_comment(self, q=None, ids=None, size=None, subreddit=None, sort_type='created_utc', after=None, before=None):
		url = 'https://api.pushshift.io/reddit/search/comment/?'
		is_first = True
		if q is not None:
			url += 'q=' + q + '&'
		if ids is not None:
			url += 'ids=' + ids + '&'
		if size is not None:
			url += 'size=' + size + '&'
		if subreddit is not None:
			url += 'subreddit=' + subreddit + '&'
		if sort_type is not None:
			url += 'sort_type=' + sort_type + '&'
		if after is not None:
			url += 'after=' + after + '&'
		if before is not None:
			url += 'before=' + before + '&'

		if url[-1] =='&':
			url = url[:-1]

		return url

	def get_url_submission(self, q=None, size=None, subreddit=None, sort_type='created_utc', after=None, before=None):
		url = 'https://api.pushshift.io/reddit/search/submission/?'
		is_first = True
		if q is not None:
			url += 'q=' + q + '&'
		if size is not None:
			url += 'size=' + size + '&'
		if subreddit is not None:
			url += 'subreddit=' + subreddit + '&'
		if sort_type is not None:
			url += 'sort_type=' + sort_type + '&'
		if after is not None:
			url += 'after=' + after + '&'
		if before is not None:
			url += 'before=' + before + '&'

		if url[-1] =='&':
			url = url[:-1]

		return url

	def get_url_comment_ids(self, submission_ids):
		return 'https://api.pushshift.io/reddit/submission/comment_ids/' + submission_ids

import pandas as pd

sub1 = pd.read_csv('submissions.csv')
sub2 = pd.read_csv('submissions_2.csv')

sub1 = pd.DataFrame(sub1, columns=['id','title','selftext','subreddit','created_utc'])
sub2 = pd.DataFrame(sub2, columns=['id','title','selftext','subreddit','created_utc'])

final_sub = sub1.append(sub2, ignore_index=True)
final_sub.to_csv('all_submissions.csv')
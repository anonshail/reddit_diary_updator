import praw

def init_subreddit():
	"this function is used to initialise a reddit instnace"

	reddit = praw.Reddit(client_id='rVcffNvW_kXs3g',
                     client_secret='KmQV2ldcsS0vkIHmdwGF1BrZNNs',
                     password='thisisapassword',
                     user_agent='testscript by /u/kurithesheep',
                     username='diaryupdator')

	return reddit

reddit = init_subreddit()
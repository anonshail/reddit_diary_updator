import praw
import time

def init_subreddit():
	"this function is used to initialise a reddit instnace"

	reddit = praw.Reddit(client_id='rVcffNvW_kXs3g',
                     client_secret='KmQV2ldcsS0vkIHmdwGF1BrZNNs',
                     password='thisisapassword',
                     user_agent='testscript by /u/kurithesheep',
                     username='diaryupdator')

	return reddit

reddit = init_subreddit()		#obtaining a reddit object
post_title = time.asctime()		#post title, which is set to the current date and time
self_text = input("please enter the text you wish to submit:\n")

sure = input("Submit? (y/n) ")

if(sure == 'y' or sure == 'Y'):
	reddit.subreddit('DiaryOfMyLife').submit(post_title, selftext = self_text)
	print("Submission made succesfully!")

else:
	print("Exitting . . .")
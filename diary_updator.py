import praw
import time
import sys

def init_subreddit():
	"this function is used to initialise a reddit instnace"

	reddit = praw.Reddit(client_id='pl',
                     client_secret='pl',
                     password='pl',
                     user_agent='lmao this works somehow!',
                     username='pl')

	return reddit

reddit = init_subreddit()		#obtaining a reddit object
post_title = time.asctime()		#post title, which is set to the current date and time
print("please enter the text you wish to submit(Ctrl+D to end submission):")

userInput = sys.stdin.readlines()	#creating a list of lines/paras
self_text=""

for i in userInput:				#forming one single submissions string
	self_text += i

sure = input("Submit? (y/n) ")

if(sure == 'y' or sure == 'Y'):
	reddit.subreddit('DiaryOfMyLife').submit(post_title, selftext = self_text)
	print("Submission made succesfully!")

else:
	print("Exitting . . .")

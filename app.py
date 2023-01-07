import praw

reddit = praw.Reddit(
    user_agent="toss-bot v1.0 by Head-Writing4678",
    client_id="8EWq-2oS1ONFlihlZ82jrQ",
    client_secret="lugNAHUNB0VJ8sTvM3ToU7UtangCKQ",
    username="toss-bot",
    password="boticelli8686"
)

#getting each submission in a specific subreddit, starting with test
subreddit = reddit.subreddit('test')
for submission in subreddit.stream.submissions():
    process_submission(submission)

def process_submission(sub):
    sub.comments.replace_more(limit=None) #this removes the 'more comments' link in the comments list

    # this gives us access to a flattened version of every comment
    for comment in sub.comments.list():
        #some functionality here












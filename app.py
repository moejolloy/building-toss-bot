import praw
import time

reddit = praw.Reddit(
    user_agent="toss-bot v1.0 by Head-Writing4678",
    client_id='8EWq-2oS1ONFlihlZ82jrQ',
    client_secret='lugNAHUNB0VJ8sTvM3ToU7UtangCKQ',
    username="toss-bot",
    password=''
)

cache = []


def process_submission(sub):
    sub.comments.replace_more(limit=None)  # this removes the 'more comments' link in the comments list

    # this gives us access to a flattened version of every comment within a submission
    for comment in sub.comments.list():
        if hasattr(comment, 'body'):
            comment_lower = comment.body.lower()
            print(comment_lower)
            if "the toss" in comment_lower and comment.id not in cache:
                print(comment_lower)
                comment.reply('HELLO!')
                cache.append(comment.id)
                time.sleep(5)


# getting each submission in a specific subreddit, starting with test
subreddit = reddit.subreddit('test')

for submission in subreddit.stream.submissions():
    process_submission(submission)

# some helpful links: https://praw.readthedocs.io/en/v7.6.1/tutorials/comments.html
# https://stackoverflow.com/questions/44729350/invalid-grant-error-processing-request-while-making-a-reddit-bot

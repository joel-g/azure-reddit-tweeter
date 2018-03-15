import tweepy, praw, time
# IMPORT SOME STUFF

with open('config.ini','r') as config:
  tokens = config.readlines()
  TW_CONSUMER_KEY = tokens[0].rstrip()
  TW_CONSUMER_SECRET = tokens[1].rstrip()
  TW_ACCESS_KEY = tokens[2].rstrip()
  TW_ACCESS_SECRET = tokens[3].rstrip()
  REDDIT_APP = tokens[4].rstrip()
  REDDIT_USER = tokens[5].rstrip()

def authenticate_twitter():
  print('Authenticating twitter...')
  auth = tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
  auth.set_access_token(TW_ACCESS_KEY, TW_ACCESS_SECRET)
  twitter = tweepy.API(auth)
  print('Twitter authenticated.\n')
  return twitter

def authenticate_reddit():
    print('Authenticating reddit...\n')
    reddit = praw.Reddit(REDDIT_APP, user_agent=REDDIT_USER)
    print('Reddit authenticated.\n')
    return reddit

def get_reddit_posts(reddit):
  print("Fetching new posts...")
  time.sleep(1)
  posts = []
  for post in reddit.subreddit('azure').hot(limit=12):
    if "reddit.com" in post.url:
      posts.append(post)
  print("Returning " + str(len(posts)) + " reddit posts")
  return posts
    
def record_already_tweeted(submission_id):
  print("Logging tweet...")
  writeable = open("tweeted.txt", 'a+')
  writeable.write(submission_id + '\n')
  writeable.close()
  time.sleep(2)
  
def is_tweeted(submission_id):
  print("Checking to see if this has already been tweeted...")
  time.sleep(1)
  readable = open("tweeted.txt", "r")
  if submission_id in readable.read().splitlines():
    print("It has been tweeted.\n")
    time.sleep(1)
    return True
  else:
    print("It has not been tweeted.\n")
    time.sleep(1)
    return False

def tweet(twitter, submission):
  print("Tweeting...")
  try:
    twitter.update_status(submission.title + " " + submission.url)
    record_already_tweeted(submission.id)
    print("Tweeted!\n")
  except:
    print("I was not able to TWEET!")
    record_already_tweeted(submission.id + "FAILURE")
  time.sleep(2)
  
def main():
  reddit = authenticate_reddit()
  twitter = authenticate_twitter()
  while True:
    for post in get_reddit_posts(reddit):
      if not is_tweeted(post.id):
        tweet(twitter, post)
        print("Sleeping 3 hours...\n\n")
        time.sleep(10800)
        break

if __name__ == '__main__':
  main()
import tweepy, praw

def authenticate_twitter():
  config = open('config.ini','r')
  tokens = config.readlines()
  config.close()
  CONSUMER_KEY = tokens[0].rstrip()
  CONSUMER_SECRET = tokens[1].rstrip()
  ACCESS_KEY = tokens[2].rstrip()
  ACCESS_SECRET = tokens[3].rstrip()
  print('Authenticating twitter...')
  auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
  auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
  twitter = tweepy.API(auth)
  print('Twitter authenticated.')
  return twitter

def authenticate_reddit():
    print('Authenticating reddit...\n')
    reddit = praw.Reddit('animal-facts-bot', user_agent='/u/AnimalFactsBot')
    print('Reddit authenticated.')
    return reddit





def main():
  reddit = authenticate_reddit()
  twitter = authenticate_twitter()

if __name__ == '__main__':
  main()

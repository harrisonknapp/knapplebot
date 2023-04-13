import tweepy
import openai

OPENAI_KEY = open("auth/openai_key.txt").read().strip()
TWITTER_CONSUMER_KEY = open("auth/twitter_consumer_key.txt").read().strip()
TWITTER_CONSUMER_SECRET = open("auth/twitter_consumer_secret.txt").read().strip()
TWITTER_ACCESS_KEY = open("auth/twitter_access_key.txt").read().strip()
TWITTER_ACCESS_SECRET = open("auth/twitter_access_secret.txt").read().strip()
OPENAI_MODEL = open("auth/openai_model.txt").read().strip()

openai.api_key = OPENAI_KEY

twitter_client = tweepy.Client(consumer_key=TWITTER_CONSUMER_KEY,consumer_secret=TWITTER_CONSUMER_SECRET,access_token=TWITTER_ACCESS_KEY,access_token_secret=TWITTER_ACCESS_SECRET)

prompt = "tweet:"

# Tweet generation

response = openai.Completion.create(
   prompt=prompt,
   model=OPENAI_MODEL,
   temperature=0.55,
   n=1,
   max_tokens=50
)

print(response)
print('\n')

tweet_text = response.choices[0].text
tweet_text = tweet_text[:280]

tweet_info = twitter_client.create_tweet(text=tweet_text,user_auth=True)

print(f'Posted tweet "{tweet_text}"')
print(f'Tweet ID: {tweet_info.id}')

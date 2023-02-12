import tweepy

# Twitter API credentials
consumer_key = "YOUR_CONSUMER_KEY"
consumer_secret = "YOUR_CONSUMER_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"

# Authenticate to Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create API object
api = tweepy.API(auth)

# Tweet ID
tweet_id = "1307692788126760960"

# Get replies for the specified tweet
replies = []
for tweet in tweepy.Cursor(api.search, q=f"to:YOUR_TWITTER_HANDLE in_reply_to_status_id:{tweet_id}", tweet_mode='extended').items(100):
    if 'in_reply_to_status_id' in tweet._json and tweet._json['in_reply_to_status_id'] == tweet_id:
        replies.append(tweet._json["full_text"])

# Print the replies
for reply in replies:
    print(reply)

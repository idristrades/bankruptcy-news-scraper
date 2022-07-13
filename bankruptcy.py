import snscrape.modules.twitter as sntwitter
import pandas as pd

query = "insolvency OR bankruptcy since:2022-07-12   from:newsfilterio OR from:fastestalert OR from:WSJbankruptcy"
tweets = []
limit = 7

for tweet in sntwitter.TwitterSearchScraper(query).get_items():

    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date,tweet.user.username, tweet.content, tweet.tcooutlinks])
        
df = pd.DataFrame(tweets, columns=['Date', 'Username', 'Tweet', 'Url'])
print(df)

#to save the data, use df.to_csv('tweets.csv')

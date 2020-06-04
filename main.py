import random
import facebook
import schedule
import time
import tweepy

#FB Access Token
accesstoken = ''

# Twitter Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

#choosing a random word from text file.
k = 1
filename = 'words.txt'
with open(filename) as file:
    lines = file.read().splitlines()

if len(lines) > k:
    random_lines = random.sample(lines, k)
    chosenline = "\n".join(random_lines)
    chosenlinestr = str(chosenline)
    message = "Fuck " + chosenlinestr 
    print(message)

    with open(filename, 'w') as output_file:
        output_file.writelines(line + "\n"
                               for line in lines if line not in random_lines)
#let's post it
def post():
    #Facebook stuff
    graph = facebook.GraphAPI(accesstoken)
    post_id = graph.put_object(parent_object='me', connection_name='feed', message = message)
    print(f"Submitted \"{message}\" on Facebook successfully!")
    #Twitterstuff
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret) 
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    # Creates the user object. The me() method returns the user whose authentication keys were used.
    user = api.me()
    # select post
    status = message  
    # Send the tweet.
    api.update_status(status)
    print(f"Submitted \"{message}\" on Twitter successfully!")
    print(f"Updates next post in 60 minutes.")

if __name__ == '__main__':
    schedule.every().hour.do(post).run()
    while 1:
        schedule.run_pending()
        time.sleep(1)

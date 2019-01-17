#Importing tweepy classes.

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import twitter_credential
#Sys library to get that output into a file
import sys

#Creating MyStreamListenerclass
class MyStreamListener(StreamListener):
    
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False


#Main method.

if __name__=="__main__" :
#Creating object of myStreamListener.
    myStreamListener= MyStreamListener()
#Adding credentials, referencing twitter_credential file.
auth=OAuthHandler(twitter_credential.Consumer_Key, twitter_credential.Consumer_Key_Secret)
auth.set_access_token(twitter_credential.Access_Token, twitter_credential.Access_Token_Secret)
stream=Stream(auth, myStreamListener)
#Function to search for a tweet having particular word. For example: Donald trump.
stream.filter(track=['9 year challenge'])
sys.stdout = open('output.json', 'w')      #To copy output to file
#print 'test'
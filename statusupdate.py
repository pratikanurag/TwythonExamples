
from twython import Twython

app_key = "CONSUMER_KEY"
app_secret = "CONSUMER_SECRET"
oauth_token = "ACCESS_TOKEN"
oauth_token_secret = "ACCESS_SECRET"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

twitter.update_status(status="Hello Twython")
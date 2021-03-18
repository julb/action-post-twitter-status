#!/usr/bin/python3
import os
import tweepy


def main():
    """ The main method executed. """

    # Input variables
    input_message = os.environ.get('INPUT_MESSAGE')
    input_twitter_app_consumer_api_key = os.environ.get('INPUT_TWITTER_APP_CONSUMER_API_KEY')
    input_twitter_app_consumer_api_secret_key = os.environ.get('INPUT_TWITTER_APP_CONSUMER_API_SECRET_KEY')
    input_twitter_app_access_token = os.environ.get('INPUT_TWITTER_APP_ACCESS_TOKEN')
    input_twitter_app_access_token_secret = os.environ.get('INPUT_TWITTER_APP_ACCESS_TOKEN_SECRET')

    # Login to Twitter.
    tweepy_oauth_handler = tweepy.OAuthHandler(input_twitter_app_consumer_api_key, input_twitter_app_consumer_api_secret_key)
    tweepy_oauth_handler.set_access_token(input_twitter_app_access_token, input_twitter_app_access_token_secret)

    # Create API handler.
    tweepy_api = tweepy.API(tweepy_oauth_handler)

    # Update status.
    tweepy_status = tweepy_api.update_status(status=input_message)

    # Print outputs
    print(f"::set-output name=id::{tweepy_status.id}")


if __name__ == "__main__":
    main()

# importing libraries and modules

import tweepy
import time
import datetime
from app.config import create_api
from time import ctime
import random


def limit_handler(cursor):
    '''
    function to handle twitter rate limits
    '''
    try:
        while True:
            yield cursor.next()

    except  tweepy.RateLimitError:

        time.sleep(1000)


def public_tweets(api):
    '''

    Weekly public tweets to remind followers of gitchat time
    Takes in the api argument

    '''

    time_difference_str = 'GMT: 20:00' + '\n' + 'CDT: 14:00' + '\n' + 'WAT: 21:00' + '\n' + 'PACIFIC TIME: 12:00'

    tweet_to_publish = [

        f'Hello everyone,it\'s almost time for #gischat :) \n Check your timezone below: \n {time_difference_str}',

        f'Hi everyone, it\'s #gischat in 30minutes :) \n Check your timezone below: \n {time_difference_str}',

        f'Hi there,don\'t forget it\'s almost #gischat time! \n Check your timezone below: \n {time_difference_str}',

        f'Join #gischat today and every Wednesday! \n It\'s a weekly twitter chat about all '
        f'things geospatial & GIS.\n Check your timezone below: {time_difference_str}\n'

    ]

    try:

        if datetime.date.today().weekday() == 2 and ctime()[11:16] == '19:30':

            random_tweet = random.choice(tweet_to_publish)

            api.update_status(random_tweet)

            print('Wednesday Tweet was successful')

        #Friday tweet
        elif datetime.date.today().weekday() == 4 and ctime()[11:16] == '14:30':

            daily_tweets = 'Hi there!\nCheck my TL for frequent and up-to-date #gischat tweets. Kindly offer help ' \
                           'where necessary! \nThank you! '

            api.update_status(daily_tweets)

            print('Friday Tweet was successful')

        #Tuesday Tweet

        elif datetime.date.today().weekday() == 1 and ctime()[11:16] == '17:30':

            daily_tweets = 'Hi there!\nCheck my TL for frequent and up-to-date #gischat tweets. Kindly offer help ' \
                           'where necessary! \nThank you! '

            api.update_status(daily_tweets)

            print('Tuesday Tweet was successful')

    except tweepy.TweepError as e:

        print('Error Message : ', e)

# MEME TWEET BLOCK
# def tweet_memes(api):
#     # Tweeting GIS memes every three days
#     # day 1->Monday
#     try:
#         # creating the filepaths
#
#         file_path = './memes'
#
#         # looping through folder select
#
#         selected=[]
#
#         file_name = [os.path.join(file_path, name) for name in os.listdir(file_path) if name.endswith('.jpg')]
#
#         image = random.choice(file_name)
#         if datetime.date.today().weekday() == 0 and ctime()[11:16] == '13:30':
#             if image not in selected:
#                 image_id = api.media_upload(image)
#
#                 api.update_status(status='😂 #gischat #gismeme #gismemes\n(Source:www.pinterest.com/tablrk2012/gis/)\n',
#                               media_ids=[image_id.media_id])
#                 selected.append(image)
#                 print('Posted successfully')
#
#         # day 2->Wednesday
#
#         elif datetime.date.today().weekday() == 2 and ctime()[11:16] == '18:15 ':
#
#             if image not in selected:
#                 image_id = api.media_upload(image)
#                 api.update_status(status='😂 #gischat #gismeme #gismemes\n(Source:www.pinterest.com/tablrk2012/gis/)\n',
#                               media_ids=[image_id.media_id])
#                 selected.append(image)
#                 print('Posted successfully')
#             else:
#                 return 'Done'
#
#         # day 3->Saturday
#
#         elif datetime.date.today().weekday() == 5 and ctime()[11:16] == '18:30':
#             if image not in selected:
#                 image_id = api.media_upload(image)
#
#                 api.update_status(status='😂 #gischat #gismeme #gismemes\n(Source:www.pinterest.com/tablrk2012/gis/)\n',
#                               media_ids=[image_id.media_id])
#                 selected.append(image)
#                 print('Posted successfully')
#             else:
#                 return 'Done'
#     except tweepy.TweepError as e:
#
#         print('Error Message: ',e )
#
#         time.sleep(900)


def follow_followers(api):

    '''
    A follower function that accepts the api,
    checks to see if a follower is being followed,
    if not, gisbot follows sback
    '''

    for follower in limit_handler(tweepy.Cursor(api.followers).items()):

        try:

            if not follower.following:
                print(f'Following ->  {follower.name}')
                follower.follow()
            else:
                print('Followed all followers')
                break

        except  tweepy.RateLimitError:
            print('Rate Limit Exceeded')
            time.sleep(900)


def main():
    api = create_api()
    while True:
        follow_followers(api)
        public_tweets(api)
        # tweet_memes(api)
        time.sleep(60)


if __name__ == '__main__':
    main()

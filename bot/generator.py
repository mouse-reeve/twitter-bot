''' Create the bot's content '''
from bot import settings
from bot.blacklist import check_blacklist

import json

def get_tweet():
    ''' create tweet content '''

    # TODO: Your neat stuff here!
    text = 'test tweet'

    # make sure it isn't posting something gross
    if check_blacklist(text):
        return False

    data = {'status': text}
    return data


def fill_queue():
    ''' populate a json file with things to post the future '''
    try:
        queue = json.load(open('%s/queue.json' % settings.FILEPATH))
    except OSError:
        queue = []

    for _ in range(0, settings.QUEUE_COUNT):
        tweet = get_tweet()
        if tweet:
            queue.append(tweet)

    json.dump(queue, open('%s/queue.json' % settings.FILEPATH, 'w'))


if __name__ == '__main__':
    if settings.USE_QUEUE:
        fill_queue()
    else:
        print(get_tweet())

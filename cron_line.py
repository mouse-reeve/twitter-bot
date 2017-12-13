''' print out a cron entry for the bot '''
from bot import settings

# populate queue
if settings.USE_QUEUE:
    print('5 */%s * * * %s/venv/bin/python3 %s/bot/generator.py' % \
            (settings.FREQUENCY, settings.FILEPATH, settings.FILEPATH))

# actual tweeting
print('0 */%s * * * %s/venv/bin/python3 %s/bot/tweet.py' % \
        (settings.FREQUENCY, settings.FILEPATH, settings.FILEPATH))

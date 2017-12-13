''' print out a cron entry for the bot '''
from bot import settings

print('0 */%s * * * %s/venv/bin/python3 %s/tweet.py' % \
        (settings.FREQUENCY, settings.FILEPATH, settings.FILEPATH))

# Twitter Bot Template

Boilerplate for creating simple, non-interactive twitter bots that post periodically. My comparisons bot, [@botaphor](https://github.com/mouse-reeve/metaphinder), is an example of how I use this template in practice.

This is intended for coders familiar with Python and bash.

## Instructions

To make a bot, copy this repo and run `start.sh` to create
a virtualenv and settings file.

When you're done (or at a stop-and-test point) with your bot,
run `ready.sh` to set up the python package and run tests.

To start tweeting on a schedule, run `python cron_lines.py` to generate
the lines you'll need to add to cron.


## Structure

The code that generates tweet content lives in the `get_tweet` method in `bot/generator.py`. Until you add your own functionality, it will tweet out "test tweet".

You will need to fill out the `bot/settings.py` that is generated when you run `start.sh`. Make sure you set an absolute path in `FILEPATH`, and fill in the API keys section with the keys you get from twitter.

If you set `USE_QUEUE` to `True` in `bot/settings.py`, a `queue.json` file will be created when the bot runs and populated with tweet data objects, which can be tweeted out later. This allows you to check what your bot will do before it goes live, and make sure that there is enough content waiting if your `get_tweet` script doesn't always produce results. The script will attempt to write 10 tweets to the queue every time it is run; you can customize this number by changing `QUEUE_COUNT`.

By default, potential tweets will be checked against a non-comprehensive list of potentially offensive words in `bot/blacklist.py`, and if the check fails, no tweet will be created or posted.

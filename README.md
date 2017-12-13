# Twitter Bot Template

Boilerplate for creating simple, non-interactive twitter bots that post periodically.

## Instructions

To make a bot, copy this repo and run `./start.sh` to create
a virtualenv and settings file.

When you're done (or at a stop-and-test point) developing your bot,
run `ready.sh` to set up the python package and run tests.

To start tweeting on a schedule, run `python cron_lines.py` to generate
the lines you'll need to add to cron.


## Structure

The code that generated what your bot will post lives in the `get_tweet` method in `bot/generator.py`.

You will need to fill out the `bot/settings.py` that is generated when you run `start.sh`. Make sure you set an absolute `FILEPATH`, and fill in the API keys section with the keys you get from twitter.

If you set `USE_QUEUE` to `True` in `bot/settings.py`, a `queue.json` file will be created when the bot runs and populated with tweet data objects, that can be posted later. This allows you to check what your bot will post before it goes live, and make sure that there is enough content waiting if your `get_tweet` script doesn't always produce results.

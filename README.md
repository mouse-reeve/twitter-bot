# Twitter Bot Template

Boilerplate for creating twitter bots.

To make a bot, copy this repo and run `./start.sh` to create
a virtualenv and settings file.

When you're done (or at a stop-and-test point) developing your bot,
run `ready.sh` to set up the python package and run tests.

To start tweeting on a schedule, run `python cron_lines.py` to generate the
scheduled task, and add those lines to cron.

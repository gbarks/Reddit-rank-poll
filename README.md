# Reddit Ranked Poll Ballot Scraper

Run a [Mitch Hawker-style](http://ushsho.com/bestrollercoasterpoll.htm) poll entirely within a Reddit comment section. Use the ballot scraper to take all top-level comments in the thread and write lines beginning with a number (such as `1, Millennium Force`) to a .txt file in a local folder. Simply run like so:

```python3 scrape_reddit_ballots.py -s SUBMISSION_ID```

where `SUBMISSION_ID` corresponds to the ID in the Reddit post URL, eg. [a31nuk](https://www.reddit.com/r/rollercoasters/comments/a31nuk/whats_the_best_bm_invert_vote_right_here_in_our)

(You can also throw in a `-v` flag if you like verbosity)

Running this requires `praw.ini` to be configured with your own `client_id` and `client_secret` tokens, which you can create yourself at https://www.reddit.com/prefs/apps
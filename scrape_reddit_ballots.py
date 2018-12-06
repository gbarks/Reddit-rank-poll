#!/usr/bin/env python3

import praw

voters = {}

reddit = praw.Reddit('ballotbot')
submission = reddit.submission(id='a31nuk')
submission.comments.replace_more(limit=None)

for top_level_comment in submission.comments:
    user = top_level_comment.author.name
    voters[user] = {}
    print('###', user)

print(len(voters), 'voters submitted a ballot')
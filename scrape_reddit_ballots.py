#!/usr/bin/env python3

import argparse
import praw
import sys
import os

# command line arguments
parser = argparse.ArgumentParser(description='Grab Reddit ballots for Mitch Hawker-style poll.')
parser.add_argument('-s', '--id', default='a31nuk', help='specify Reddit submission id')
parser.add_argument('-v', '--verbose', action='store_true', help='print ballot data in console')
args = parser.parse_args()

# collection of ballots
voters = {}

reddit = praw.Reddit('ballotbot')
submission = reddit.submission(id=args.id)
submission.comments.replace_more(limit=None)

for top_level_comment in submission.comments:
    user = top_level_comment.author.name
    voters[user] = [user, '! DO NOT CHANGE OR DELETE THIS LINE !']
    if args.verbose:
        print(user)

    for line in top_level_comment.body.splitlines():
        line = line.strip() # strip leading whitespace
        if line[:1] == '>': # strip >quote formatting
            line = line[1:].strip()
        if line[:1].isdigit():
            voters[user].append(line)
            if args.verbose:
                print('   ', line)

# name of folder where ballots are saved, don't overwrite existing folders
folder = args.id + '_ballots'
while os.path.isdir(folder):
    if folder[-1:] == ')' and '(' in folder:
        version = folder[folder.rfind('(')+1:folder.rfind(')')]
        if version.isdigit():
            num = int(version)
            num += 1
            folder = folder[:folder.rfind('(')+1] + str(num) + ')'
            continue
    folder = folder + ' (1)'

try:
    os.mkdir(folder)
except OSError:
    print('Creation of "%s" directory failed; terminating...' % folder)
    sys.exit()

# write a .txt file for each voter's ballot
for voter, ballot in voters.items():
    with open(os.path.join(folder, voter + '.txt'), 'w') as f:
        for line in ballot:
            f.write('%s\n' % line)

if args.verbose:
    print(len(voters), 'voters submitted a ballot; ballots saved in "%s"' % folder)

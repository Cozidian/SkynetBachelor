import jsonfilter
import subprocess
import os
"""
with open ("users.txt", "r") as users:
    for line in users:
        if line != "":
            tweets = twitterscraper.query.query_tweets(query=line, poolsize=1)
        if tweets:
            with open(("jsontweets/" + line + ".json"), "w") as output:
                json.dump(tweets, output, cls=JSONEncoder.JSONEncoder)
"""
# twitterscraper -l 100 -o billgates.json billgates

if not os.path.isdir("unfilteredtweets"):
    os.mkdir("unfilteredtweets")

if not os.path.isdir("filteredtweets"):
    os.mkdir("filteredtweets")

with open("users.txt", "r") as users:
    for line in users:
        if line.strip() != "" and not os.path.exists("unfilteredtweets/" + line.strip() + ".json"):
            # print(line)
            outputfile = "unfilteredtweets/" + line.strip() + ".json"
            subprocess.check_call(["twitterscraper", "-l", "100",  "-o", outputfile, line.strip()])

            if os.path.exists(outputfile):
                jsonfilter.twitterfilter((line.strip()))

# subprocess.check_call(["twitterscraper", "-l", "100",  "-o", "billgates.json", "billgates"])
# jsonfilter.twitterfilter("billgates", inputpath="")

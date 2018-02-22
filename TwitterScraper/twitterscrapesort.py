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


def main():
    # if not os.path.isdir("unfilteredtweets"):
    #    os.mkdir("unfilteredtweets")

    if not os.path.isdir("filteredtweets"):
        os.mkdir("filteredtweets")

    with open("users.txt", "r") as users:
        for line in users:
            if line.strip() != "" and not os.path.exists("filteredtweets/" + line.strip() + ".json"):
                # print(line)
                outputfile = "filteredtweets/" + line.strip() + ".json"
                subprocess.check_call(["twitterscraper", "-l", "100", "-o", outputfile, "from%3A" + line.strip()])

                # if os.path.exists(outputfile):
                #    jsonfilter.twitterfilter((line.strip()))

if __name__ == '__main__':
    main()

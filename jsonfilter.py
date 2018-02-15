import json


def twitterfilter(filename, outputpath="filteredtweets/", inputpath="unfilteredtweets/"):
    with open(inputpath + filename + ".json", "r") as f:
        data = json.load(f)
        indexs = []

        for i in range(0, len(data)):
            if data[i]["user"].lower() != filename.lower():
                indexs.append(i)

        print("Total Tweets: " + str(len(data)))
        print("Deleted tweets: " + str(len(indexs)))

        for ind in reversed(indexs):
            del data[ind]

        print("New Total Tweets: " + str(len(data)))

        with open(outputpath + "new" + filename + ".json", "w") as nf:
            json.dump(data, nf)

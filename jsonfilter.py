import json

with open("billgates.json", "r+") as f:
    data = json.load(f)
    indexs = []

    for i in range(0, len(data)):
        if(data[i]["user"].lower() != "billgates"):
            indexs.append(i)

    print("Tweets: " + str(len(data)))
    print("Tay tweets: " + str(len(data) - len(indexs)))
    print("Dels: " + str(len(indexs)))

    for ind in reversed(indexs):
        del data[ind]

    print("Tweets: " + str(len(data)))

    with open("newgates.json", "w") as nf:
        json.dump(data, nf)

import json

path = "unfilteredtweets/"

def checker(name):
    print("unfiltered")
    with open(path + name + ".json", "r") as file:
        data = json.load(file)
        count = 0
        for i in range(0, len(data)):
            if data[i]["user"].lower() == name:
                count += 1

        print("total: " + str(len(data)))
        print("correct: " + str(count))

    print("filtered")
    with open("../unfilteredtweets/" + name + ".json", "r") as file:
        data = json.load(file)
        count = 0
        for i in range(0, len(data)):
            if data[i]["user"].lower() == name:
                count += 1

        print("total: " + str(len(data)))
        print("correct: " + str(count))
        print()


def main():
    with open("users.txt", "r") as f:
        for line in f:
            if line.strip() != "":
                print(line.strip())
                checker(line.strip())

if __name__ == '__main__':
    main()

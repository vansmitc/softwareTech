import re  # Import regular expression operations library


def same(item, target):  # Declare "same" function
    return len([c for (c, t) in zip(item, target) if c == t])


def build(pattern, words, seen, list):  # Declare "build" function
    return [word for word in words
            if re.search(pattern, word) and word not in seen.keys() and
            word not in list]


def find(word, words, seen, target, path):  # Declare "find" function
    list = []
    for i in range(len(word)):
        list += build(word[:i] + "." + word[i + 1:], words, seen, list)
    if len(list) == 0:
        return False
    list = sorted([(same(w, target), w) for w in list])
    for (match, item) in list:
        if match >= len(target) - 1:
            if match == len(target) - 1:
                path.append(item)
            return True
        seen[item] = True
    for (match, item) in list:
        path.append(item)
        if find(item, words, seen, target, path):
            return True
        path.pop()


fname = input("Enter dictionary name: ")  # Prompts user to enter the dictionary file
file = open(fname)  # Opens file
lines = file.readlines()  # Reads all lines until EOF
while True:
    start = input("Enter start word:")  # Prompts user to enter starting word
    words = []  # Declare "words" list
    for line in lines:
        word = line.rstrip()  # Defines all words on each line (with chars stripped from the end)
        if len(word) == len(start):
            words.append(word)  # Appends
    target = input("Enter target word:")
    break

count = 0
path = [start]
seen = {start: True}
if find(start, words, seen, target, path):
    path.append(target)
    print(len(path) - 1, path)
else:
    print("No path found")

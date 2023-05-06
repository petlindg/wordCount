def promptFileName():
    filePath = input("Enter file path:\n")
    return filePath

def fileToString(filePath):
    file = open(filePath, 'r')
    text = file.read()
    file.close()
    return text

# counts all occurrences of words in the given 'text' and returns it as a key map.
def count(text):
    map = dict()
    endWordList = '.,.?!'
    words = text.split()
    for word in words:
        word.strip(endWordList)
        word = word.lower()
        if word in map:
            map[word]+=1
        else:
            map[word]=1
    return map

def printMap(map):
    for key in map:
        print(key + ': ' + str(map[key]))

def printLookup(word, map):
    if word in map:
        print(word + ': ' + str(map[word]))
    else:
        print("Word '" + word + "' not found.")

def main():
    text = fileToString(promptFileName())
    map = count(text)
    map = dict(sorted(map.items(), key=lambda item: item[1]))
    while True:
        answer = input("1: print word count, 2: lookup word: q: exit\n")
        if answer == '1':
            printMap(map)
        elif answer == '2':
            lookup = input("Enter word to lookup:\n")
            printLookup(lookup, map)
        else:
            break

main()
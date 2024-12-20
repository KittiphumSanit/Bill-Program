import json

def saveDATA(data,fileName):

    path = './data/' + fileName
    
    # convert into JSON:
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def readDATA(fileName):

    path = './data/' + fileName

    # Open and read the JSON file
    with open(path, 'r') as file:
        data = json.load(file)

    return data
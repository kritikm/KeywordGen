import os
from subprocess import call
# from collections import defaultdict

from result import Result

projectDir = '/home/rkb/Documents/KeywordGen/'
# songsDir = projectDir + 'songs'
# parserDir = projectDir + 'parser'
stopwordsPath = projectDir + 'stopwords'
# outputSuffix = ".output"

raw_keys = projectDir + 'raw_frequency_keys'

def term_search(searchTerms):
    stopwords = []
    results = []
    with open(stopwordsPath) as f:
        for word in f:
            stopwords.append(word)

    names = os.listdir(raw_keys)

    for name in names:
        filePath = os.path.join(raw_keys, name)
        if os.path.isfile(filePath):
            with open(filePath) as f:
                scoreDict = {}
                for term in searchTerms:
                    scoreDict[term] = 0
                for line in f:
                    keys = line.split('\t')
                    if keys[0].strip() in searchTerms:
                        print(keys[-1])
                        scoreDict[keys[0].strip()] = int(keys[-1])
            results.append(Result(filePath, scoreDict))
    return results

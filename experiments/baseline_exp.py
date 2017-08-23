import os
from subprocess import call
from collections import defaultdict

projectDir = os.path.join(os.getcwd(), '..')
songsPath = os.path.join(projectDir, 'full_set')
parserDir = os.path.join(projectDir, 'parser')
stopwordsPath = os.path.join(projectDir, 'stopwords')
raw_keys = os.path.join(projectDir, 'raw_frequency_keys')
outputSuffix = ".output"

stopwords = []
with open(stopwordsPath) as f:
    for word in f:
        stopwords.append(word)

names = os.listdir(songsPath)
for name in names:
    filePath = os.path.join(songsPath, name)
    if os.path.isfile(filePath):
        with open(filePath) as f:
            print("Extracting keywords from file %s" %name)
            call(["make", "-C", parserDir, filePath + outputSuffix])
            with open(filePath + outputSuffix) as outFile:
                keywords = defaultdict(lambda:0)
                for line in outFile:
                    if(line == "\n"):
                        continue
                    tag = line.split()
                    if tag[4] == '0' and tag[2].strip not in stopwords and len(tag[2]) > 2:
                        keywords[tag[2].strip()] += 1
            os.remove(filePath + outputSuffix)
            keywordFile = os.path.join(raw_keys, name)
            with open(keywordFile, 'w') as keyFile:
                for item in sorted(keywords.items(), key = lambda x : -x[1]):
                    keyFile.write('%s\n' %(item[0]))

            
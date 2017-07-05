import sys
import raw_frequency
import result

if len(sys.argv) == 1:
    print("No search term")
    sys.exit()

searchTerms = []
for arg in sys.argv[1:]:
    searchTerms.append(arg)

rawResults = raw_frequency.term_search(searchTerms)

for res in rawResults:
    print(res.filePath)
    # for value in sorted(res, key = lambda x: -(res.searchScores[value])):
    #     print(value)
    for value in res.searchScores:
        print('%s : %d' %(value, res.searchScores[value]))

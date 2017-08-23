import os
import rake

projectDir = os.path.join(os.getcwd(), '..')
songsPath = os.path.join(projectDir, 'full_set')
stopwordsPath = os.path.join(projectDir, 'stopwords')
rake_keys = os.path.join(projectDir, 'rake_keys')

names = os.listdir(songsPath)

for name in names:
    filePath = os.path.join(songsPath, name)
    if os.path.isfile(filePath):
        with open(filePath) as f:
            print("Extracting keywords from file %s" %name)
            text = f.read()

            rake_obj = rake.Rake(stopwordsPath)
            keywords = rake_obj.run(text)
            keywordFile = os.path.join(rake_keys, name)
            with open(keywordFile, 'w') as keyFile:
                for key in keywords:
                    keyFile.write('%s\n' %(key[0]))

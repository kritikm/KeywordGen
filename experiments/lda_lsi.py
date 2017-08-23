import gensim
import os
from gensim import corpora

projectDir = os.path.join(os.getcwd(), '..')
stopwordsPath = os.path.join(projectDir, 'stopwords')
songsPath = os.path.join(projectDir, 'full_set')
keywordsPath = os.path.join(projectDir, 'rake_keys')

songs = []
names = os.listdir(songsPath)

for name in names:
    with open(os.path.join(songsPath, name)) as f:
        song = ""
        for line in f.readlines()[5:]:
            song += line
        songs.append(song)
            
with open(os.path.join(projectDir, stopwordsPath)) as stops:
    stopwords = set(stops.read().split())

song_docs = [[word for word in song.split() if word not in stopwords] for song in songs]
dictionary = corpora.Dictionary(song_docs)
corpus = [dictionary.doc2bow(song) for song in song_docs]

#for LDA
lda = gensim.models.ldamodel.LdaModel(corpus = corpus, id2word = dictionary, num_topics = 5)
same = 0
for name, song in zip(names, songs):
    with open(os.path.join(keywordsPath, name)) as keys:
        
        song_topics = lda[dictionary.doc2bow(song.split())]
        key_topics = lda[dictionary.doc2bow(keys.read().split())]        
        if(len(key_topics) == 0 or len(song_topics) == 0):
            continue
            
        song_topic = max(song_topics, key = lambda x: x[1])[0]
        key_topic = max(key_topics, key = lambda x: x[1])[0]
        if(song_topic == key_topic):
            same += 1
print('LDA Result: %s/%s' %(same, len(names)))

#for LSI
lsi = gensim.models.lsimodel.LsiModel(corpus = corpus, id2word = dictionary, num_topics = 5)
same = 0
for name, song in zip(names, songs):
    with open(os.path.join(keywordsPath, name)) as keys:
        
        #sometimes, the keywords are too few for a document to be put in a certain category. That is when an lsi
        #returns an empty list
        song_topics = lsi[dictionary.doc2bow(song.split())]
        key_topics = lsi[dictionary.doc2bow(keys.read().split())]
        if(len(key_topics) == 0 or len(song_topics) == 0):
            continue
    
        song_topic = max(song_topics, key = lambda x: x[1])[0]
        key_topic = max(key_topics, key = lambda x: x[1])[0]
        
        if(song_topic == key_topic):
            same += 1
print('LSI Result: %s/%s' %(same, len(names)))
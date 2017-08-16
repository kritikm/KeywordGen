import os

songsDir = os.path.join(os.getcwd(), '100')
cleaned = os.path.join(os.getcwd(), 'cleaned')
names = os.listdir(songsDir)

for name in names:
	with open(os.path.join(songsDir, name)) as source:
		with open(os.path.join(cleaned, name), 'w') as res:
			for line in source.readlines()[5:]:
				res.write(line)
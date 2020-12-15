import glob
import json
import random

all_lyrics_by_song = {}
for file in glob.glob('*.json'):
  if 'lyrics_pairs.json' in file:
      continue
  data = json.load(open(file))  
  lyrics = data['lyrics'].split('\n')
  all_lyrics_by_song[file] = lyrics

lyrics_pairs = []
for x in range(0,10000):

  for song in all_lyrics_by_song:
    random.shuffle(all_lyrics_by_song[song])
    if '[Chorus]' in all_lyrics_by_song[song][0] or '[Chorus]' in all_lyrics_by_song[song][1]:
        continue
    if '[Intro]' in all_lyrics_by_song[song][0] or '[Intro]' in all_lyrics_by_song[song][1]:
        continue
    if '[Outro]' in all_lyrics_by_song[song][0] or '[Outro]' in all_lyrics_by_song[song][1]:
        continue 
    if '[Verse]' in all_lyrics_by_song[song][0] or '[Verse]' in all_lyrics_by_song[song][1]:
        continue 
    if '[Verse 2]' in all_lyrics_by_song[song][0] or '[Verse 2]' in all_lyrics_by_song[song][1]:
        continue 
    if '[Verse 3]' in all_lyrics_by_song[song][0] or '[Verse 3]' in all_lyrics_by_song[song][1]:
        continue
    if '[Verse 4]' in all_lyrics_by_song[song][0] or '[Verse 4]' in all_lyrics_by_song[song][1]:
        continue 
    if all_lyrics_by_song[song][0].strip() == "" or all_lyrics_by_song[song][1].strip() == "":
        continue
    try:
        lyrics_pairs.append(all_lyrics_by_song[song][0] + "\n" + all_lyrics_by_song[song][1])
    except:
        continue
json.dump(lyrics_pairs,open('lyrics_pairs.json','w'),indent=2)
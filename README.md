# SonicYouthBot
SonicYouthBot (@malibu_gas)

Sonic Youth was an influential experimental rock band formed in New York City in 1981. Known for their anthems, distortion, and cryptic lyrics, Sonic Youth's message remains as fresh as it was 30 years ago. This Twitterbot takes lyrics from Sonic Youth's 15 album discography and shakes it up a bit, creating something new out of the familiar. 

Sonic.Nurse.py <br> 
After attaining the GENIUS API Client, I was able to retrieve lyrics from the Genius API by using the lyricsgenius python module. I was able to get several JSON files with various Sonic Youth metadata, such as song title, release date, lyrics, songs in each file. I was only looking for the lyrics. 

Sonic2.py <br>
I created a new file that is able to loop through all the songs and add their lyrics to a big dictionary, but also creating pairs out of two random lines (lyrics_pairs.json).

Kimgithub.py <br>
Using the Twitter API to set up the bot, I was able to use the Tweepy module to create a code that would randomely tweet out lyric pairs form the lyrics_pairs.Json file. Then I uploaded it onto AWS Lambda, triggering it to tweet every hour. 

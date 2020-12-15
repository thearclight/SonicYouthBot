# SonicYouthBot
SonicYouthBot (@malibu_gas)

Sonic Youth was an influential experimental rock band formed in New York City in 1981. Known for their anthems, distortion, and cryptic lyrics, Sonic Youth's message remains as fresh as it was 30 years ago. This Twitterbot takes lyrics from Sonic Youth's 15 album discography and shakes it up a bit, creating something new out of the familiar. 


After attaining the GENIUS API Client, I was able to retrieve lyrics from the Genius API by using the lyricsgenius python module. I was able to get several JSON files with various Sonic Youth metadata, such as song title, release date, lyrics, songs in each file. I was only looking for the lyrics. 

Sonic2.Py
I created a new file that is able to loop through all the songs and add their lyrics to a big dictionary, use the random module, and print two random lyrics from each song to tweet. 


used the Twitter API to set up the actual bot that would take the lyrics element from each JSON file and print the lyrics two lines at a time. I then uploaded that file on AWS LAMBDA and set up a trigger that would send out a tweet every hour. 

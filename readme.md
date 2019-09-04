# What is 'Who Do You LoveListening To?'

'Who Do You Love Listening To?' is a Python program that uses the Python port of Spotify API, Spotipy, to display what artists you've listened to the most over three terms: long, medium and short.

The program utilizes OAuth2 included in the Spotify API for authentication. 

A graph will be saved in the project folder that showcases all the artists in your top tracks along with how many different songs of theirs you have listened to.



# Usage
Run:

`pip install -r requirements.txt`

Edit line 56 of MainApp.py with a clientID and secret clientID from a spotify developer account (https://developer.spotify.com/)

Then run:
`MainApp.py spotifyuserURL`

spotifyuserURL is your Spotify profile's URL. 



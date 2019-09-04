import spotipy
import sys
import spotipy.util as util
import webbrowser
import matplotlib.pyplot as plt
import simplejson as json
import pandas as pd

scope = 'user-top-read'
TopArtistList = []
TopArtistDict = []
ArtistCount = []
continueloop = True


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0]))
    sys.exit()

print("Welcome to Who Do You Love Listening To")
print("Term choices:")
print("1. Long Term")
print("2. Medium Term")
print("3. Short Term")


while(continueloop == True):
    choice = input("Enter your choice:")

    if choice == '1':
        term = "long_term"
        continueloop = False

    if choice == '2':
        term = "medium_term"
        continueloop = False

    if choice == '3':
        term = "short_term"
        continueloop = False

    else:
        print("invalid")









token = util.prompt_for_user_token(username, scope, client_id='XXXXXXXXXXXXXXXX', client_secret='XXXXXXXXXXXXXXXXXX', redirect_uri='http://google.com/')

if token:
    sp = spotipy.Spotify(auth=token)
    results = sp.current_user_top_tracks(time_range=term, limit=25)
    print("Your Top 25 Songs Are:")
    for item in results['items']:
        print(item['name'] + ' // ' + item['artists'][0]['name'])
        itemstr = item['artists'][0]['name']
        TopArtistList.append(itemstr)


else:
    print("could not acquire token for", username)


artistseries = pd.Series(TopArtistList)

artistseries = artistseries.value_counts()

artistseries.plot.bar(color='#1DB954',edgecolor='black')

plt.xlabel('Artists', fontsize = 18)
plt.ylabel('# of songs listened', fontsize=16)

plt.savefig("YourFavoriteArtists.png", bbox_inches='tight', dpi=100)
print("A graph has been generated and saved in the project folder...")
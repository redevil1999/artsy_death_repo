import json

with open('something.json', encoding= 'utf-16') as file:
    data_musical_artist = json.load(file)

musical_artist = []

for artist in data_musical_artist:
    if artist['musical artist']:
        musical_artist.append(artist)
    elif artist['MusicalArtist']:
        musical_artist.append(artist)
    elif artist['musicalArtist']:
        musical_artist.append(artist)
    elif artist['MusicGroup']:
        musical_artist.append(artist)
    elif artist['musician']:
        musical_artist.append(artist)

musical_artist_birth_year = []

for artist in musical_artist_selected:
    if artist['ontology/birthYear'] >= 1915:
        musical_artist_birth_year.append(artist)
    if artist


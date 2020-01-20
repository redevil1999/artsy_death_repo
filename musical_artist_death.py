# import json

# with open('filtered_music.json', encoding= 'utf8') as file:
#     data_musical_artist = json.load(file)

# musical_artist = []

# for artist in data_musical_artist:
#     if artist['musical artist']:
#         musical_artist.append(artist)
#     elif artist['MusicalArtist']:
#         musical_artist.append(artist)
#     elif artist['musicalArtist']:
#         musical_artist.append(artist)
#     elif artist['MusicGroup']:
#         musical_artist.append(artist)
#     elif artist['musician']:
#         musical_artist.append(artist)

# musical_artist_age = []

# for artist in musical_artist_selected:
#     if artist['ontology/birthYear'] >= 1915:
#         musical_artist_age.append(artist)
#         musical_artist_age.append(artist['ontology/deathYear'])

musical_artist_age = [
    {'ontology/birthYear': '1998',
    'ontology/deathYear': '2015'},
    {'ontology/birthYear': '1880',
    'ontology/deathYear': '1999'
    }
]

with open('musical_artist_age.csv', 'w', encoding= 'utf8') as file: 
    file.write('birthYear, deathYear, \n')
    for entry in musical_artist_age: 
            file.write(f"{entry['ontology/birthYear']}, {entry['ontology/deathYear']}\n")

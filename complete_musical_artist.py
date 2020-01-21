import json
import os

musical_artist = []

for filename in os.listdir('People'):
    with open(f'People/{filename}', encoding= 'utf8') as file:
        data_musical_artist = json.load(file)
        

        for artist in data_musical_artist:
            if "musical artist" in artist['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']:
                musical_artist.append(artist)
            elif "http://dbpedia.org/ontology/MusicalArtist" in artist['http://www.w3.org/1999/02/22-rdf-syntax-ns#type']:
                musical_artist.append(artist)
            elif "MusicGroup" in artist['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']:
                musical_artist.append(artist)
            elif 'http://purl.org/dc/elements/1.1/description' in artist and "musician" in artist['http://purl.org/dc/elements/1.1/description']:
                musical_artist.append(artist)
            elif 'http://purl.org/dc/elements/1.1/description' in artist and "composer" in artist['http://purl.org/dc/elements/1.1/description']:
                musical_artist.append(artist)
            elif 'ontology/associatedBand_label' in artist:
                musical_artist.append(artist)
            elif 'ontology/associatedBand' in artist:
                musical_artist.append(artist)
            elif 'ontology/occupation' in artist and "http://dbpedia.org/resource/Composer" in artist['ontology/occupation']:
                musical_artist.append(artist)
            elif 'ontology/occupation_label' in artist and "Composer" in artist['ontology/occupation_label']:
                musical_artist.append(artist)
            elif 'ontology/associatedMusicalArtist_label' in artist:
                musical_artist.append(artist)

# for artist in musical_artist:
#     if 'ontology/birthDate' in artist:
#         birthdate = str(artist['ontology/birthDate'])
#         birthdate.split('-')
#         artist['birthDate'] = birthdate[0:4]
#     elif 'ontology/deathDate' in artist:
#         deathdate = str(artist['ontology/deathDate'])
#         deathdate.split('-')
#         artist['deathDate'] = deathdate[0:4]

with open('musical_artist.csv', 'w', encoding= 'utf8') as file: 
    file.write('birthYear, deathYear \n')
    for entry in musical_artist: 
        if 'ontology/birthYear' in entry and 'ontology/deathYear' in entry:
            file.write(f'{entry["ontology/birthYear"]}, {entry["ontology/deathYear"]}\n')
        # else:
        #     if 'birthDate' in entry and 'deathDate' in entry:
        #         file.write(f'{entry["birthDate"]}, {entry["deathDate"]}\n')
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

with open('musical_artist_country.csv', 'w', encoding= 'utf8') as file: 
    file.write('birthYear, deathYear, country \n')
    for entry in musical_artist:
        if 'ontology/birthYear' in entry:
            birthYear = entry["ontology/birthYear"]
            if 'ontology/deathYear' in entry:
                deathYear = entry["ontology/deathYear"]
                if 'ontology/country_label' in entry:
                    country = entry['ontology/country_label']
                elif 'ontology/country' in entry:
                    country = entry['ontology/country']
                elif 'ontology/nationality_label' in entry:
                    country = entry['ontology/nationality_label']
                elif 'ontology/nationality' in entry:
                    country = entry['ontology/nationality']
                elif  'ontology/birthPlace' in entry:
                    country = entry['ontology/birthPlace']
                elif 'ontology/birthPlace_label' in entry:
                    country = entry['ontology/birthPlace_label']
                else:
                    country = "NA"
                if type(country) == list:
                    country_clean = country[0]
                else:
                    country_clean = country
                file.write(f'{birthYear},{deathYear},{country_clean}\n')

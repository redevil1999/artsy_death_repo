import json
import os

athletes = []

for filename in os.listdir('People'):
    if filename.endswith('.json'):
        with open(f'People/{filename}', encoding = 'utf8') as file:
            data_athletes = json.load(file)
        
            for athlete in data_athletes:
                if "athlete" in athlete['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']:
                    athletes.append(athlete)
                elif "http://dbpedia.org/ontology/SportsTeamMember" in athlete['http://www.w3.org/1999/02/22-rdf-syntax-ns#type']:
                    athletes.append(athlete)
                elif 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label' in athlete and "Sports team member" in athlete['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']:
                    athletes.append(athlete)
                elif 'ontology/discipline_label' in athlete:
                    athletes.append(athlete)
                elif 'olympic' in athlete:
                    athletes.append(athlete)


for athlete in athletes:
    if 'ontology/birthDate' in athlete:
        birthdate = str(athlete['ontology/birthDate'])
        birthdate.split('-')
        athlete['birthDate'] = birthdate[0:4]
    elif 'ontology/deathDate' in athlete:
        deathdate = str(athlete['ontology/deathDate'])
        deathdate.split('-')
        athlete['deathDate'] = deathdate[0:4]

with open('athletes.csv', 'w', encoding= 'utf8') as file: 
    file.write('birthYear, deathYear \n')
    for entry in athletes: 
        if 'ontology/birthYear' in entry and 'ontology/deathYear' in entry:
            file.write(f'{entry["ontology/birthYear"]}, {entry["ontology/deathYear"]}\n')
        else:
            if 'birthDate' in entry and 'deathDate' in entry:
                file.write(f'{entry["birthDate"]}, {entry["deathDate"]}\n')
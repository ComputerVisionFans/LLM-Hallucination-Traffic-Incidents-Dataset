import json
import re


# Load the JSON data from the uploaded file
file_path = './original/Wiener_2013-2023.json'

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Checking the structure of the JSON data
data.keys(), type(data), isinstance(data, list)

# Looking at the first few entries under 'incidents' to understand the structure
first_incidents = data['incidents'][:3]  # Just to get a snippet of the data
first_incidents

def index_description_sentences(incident_data):
    """
    This function takes a list of incidents and adds an index to each sentence in the 'description' field.
    """
    for incident in incident_data:
        # Check if 'description' exists in the incident
        if incident['description']:
            # Split the description into sentences
            sentences = re.split(r'(?<=[.!?])\s+', incident['description'])
            indexed_sentences = []
            # Add an index to each sentence
            for idx, sentence in enumerate(sentences, 1):
                # Ensure the sentence is non-empty after splitting
                if sentence.strip():
                    indexed_sentence = f"{idx}. {sentence}"
                    indexed_sentences.append(indexed_sentence)
            # Join the indexed sentences back into a single string
            incident['description'] = ' '.join(indexed_sentences)
    return incident_data

# Index the sentences in the 'description' field of each incident
indexed_incidents = index_description_sentences(data['incidents'])

# Save the modified data to a new JSON file
output_file_path = './hypotheise/hypotheise_1.json'
with open(output_file_path, 'w', encoding='utf-8') as new_file:
    json.dump({'incidents': indexed_incidents}, new_file, ensure_ascii=False, indent=2)

output_file_path


import json

#The string "Die U-Bahnlinie U3 kann wegen eines schadhaften Fahrzeuges derzeit in beiden Richtungen nur unregelmäßig fahren" appears to be improperly encoded, resulting in distorted characters. Specifically, "unregelmäßig" is being displayed as "unregelmÃ¤Ãig". This kind of issue typically occurs when text encoded in UTF-8 is incorrectly interpreted using a different encoding standard, such as ISO-8859-1 or Windows-1252.

#In UTF-8 encoding, German characters like "ä" and "ß" are represented as multi-byte sequences. If a system interprets these bytes using a single-byte encoding like ISO-8859-1 or Windows-1252, each byte of the multi-byte sequence is displayed as a separate character, leading to garbled text.

#To correctly display the text, it should be interpreted or converted back to UTF-8 encoding. This would correct the representation of characters such as "ä" and "ß". If you have access to the source of this text or the system displaying it, ensuring that UTF-8 encoding is used throughout (both for reading and displaying the text) should resolve the issue.


# Reload the JSON data from the uploaded file due to code execution state reset
file_path_german = './original/Wiener_2013-2023.json'

# Function to replace German special characters with their English equivalents
def replace_german_characters(text):
    replacements = {
        'ä': 'ae',
        'ü': 'ue',
        'ö': 'oe',
        'ß': 'ss',
        'Ä': 'Ae',
        'Ü': 'Ue',
        'Ö': 'Oe'
    }
    for german_char, english_char in replacements.items():
        text = text.replace(german_char, english_char)
    return text

# Read the content of the file and apply the replacement
with open(file_path_german, 'r', encoding='utf-8') as file:
    german_data = json.load(file)

# Apply the replacement to all string values in the JSON data
def replace_german_chars_in_json(data):
    if isinstance(data, dict):
        return {k: replace_german_chars_in_json(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_german_chars_in_json(element) for element in data]
    elif isinstance(data, str):
        return replace_german_characters(data)
    else:
        return data

# Re-open the original German JSON file with the correct encoding
with open(file_path_german, 'r', encoding='utf-8') as file:
    german_data = json.load(file)

# Re-apply the replacement to all string values in the JSON data using the correct encoding
german_data_replaced_correctly = replace_german_chars_in_json(german_data)

# Save the correctly modified data to a new JSON file
output_file_path_german_corrected = './hypotheise/hypotheise_3.json'
with open(output_file_path_german_corrected, 'w', encoding='utf-8') as new_file:
    json.dump(german_data_replaced_correctly, new_file, ensure_ascii=False, indent=2)

output_file_path_german_corrected



def translate_text(text, source_lang='de', target_lang='en'):
    """
    Translates the given text from source language to target language.
    This is a placeholder function. In a real scenario, this function would
    integrate with a translation API like Google Translate.
    """
    # Placeholder: replace with actual translation code
    translated_text = "This is a translated text."  # Dummy translation
    return translated_text

def translate_descriptions_in_json(file_path, output_file_path):
    # Read the JSON file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Iterate over each item and translate the description
    for item in data:
        if 'description' in item:
            german_description = item['description']
            english_description = translate_text(german_description)
            item['description'] = english_description

    # Write the translated data back to a new JSON file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)

# Example usage
file_path = 'path_to_your_json_file.json'
output_file_path = 'path_to_output_json_file.json'
translate_descriptions_in_json(file_path, output_file_path)

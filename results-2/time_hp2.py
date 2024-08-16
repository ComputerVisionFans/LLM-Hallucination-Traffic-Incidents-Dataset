import re
from datetime import datetime
import json
# Load the JSON data from the uploaded file
file_path = './original/Wiener_2013-2023.json'

# Read the content of the file
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Checking the structure of the JSON data
data.keys(), type(data), isinstance(data, list)

def convert_dates_in_text(text):
    """
    This function searches for dates and times in the text and converts them to a human-readable format.
    """
    # Define a regular expression pattern for dates and times
    # This pattern looks for strings like '2023-08-17 13:16:50' and '2023-08-17'
    date_time_pattern = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})(?:\s+(\d{2}):(\d{2})(?::(\d{2}))?)?\b')

    def replace_with_human_readable(match):
        """
        This is a helper function that will be called for each regex match.
        """
        year, month, day, hour, minute, second = match.groups()
        # Convert to human-readable format
        date_str = f"{year} Year {int(day)}th of {datetime.strptime(month, '%m').strftime('%B')}"
        if hour and minute:  # If the pattern includes a time
            time_str = f"{int(hour)} oclock {int(minute)} mins"
            time_str += f" {int(second)} seconds" if second else ""
            return f"{date_str} {time_str}"
        return date_str

    # Replace all matches in the text with the human-readable format
    return date_time_pattern.sub(replace_with_human_readable, text)

# Apply the conversion to the 'description' field of each incident
for incident in data['incidents']:
    if incident['description']:
        incident['description'] = convert_dates_in_text(incident['description'])

def human_readable_date(date_str):
    """
    Converts a datetime string to a human-readable format.
    If the input is empty, returns an empty string.
    """
    if not date_str:
        return ''
    try:
        # Parse the datetime string into a datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
        # Convert to the human-readable format
        return date_obj.strftime('%Y years %dth of %B %H oclock %M mins %S seconds')
    except ValueError:
        # If the date string is not in the expected format, return it unmodified
        return date_str

# Apply the conversion to the 'start', 'trafficStart', and 'end' fields
for incident in data['incidents']:
    for time_key in ['start', 'traffic_start', 'end']:
        if time_key in incident and incident[time_key]:
            incident[time_key] = human_readable_date(incident[time_key])


# Save the modified data to a new JSON file
new_file_path_with_descriptions = './hypotheise/hypotheise_2.json'
with open(new_file_path_with_descriptions, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

new_file_path_with_descriptions

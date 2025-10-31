import re
import json

# Removes undesired characters often found at the beginning/end of lines in our OCR scan
def clean(s):
    if not s:
        return None
    s = re.sub(r"[\d\*\s\.,;:\"'?!>]+$", "", s.strip())
    s = re.sub(r"TM+$", "", s)
    return s.strip()


with open("text_clean.txt", "r") as file:
    text = file.read()

# Splits file into entries (every final line in an entry begins with "Listed as", so we use that as separator)
entries = re.split(r"(?m)^\s*Listed as*s", text)
entries = [e.strip() for e in entries if e.strip()]
entries.pop()

# Regex patterns used to extract data
title_pattern = r"(?m)^(?:\d{4}/\d{1,2}\s+)?(.+?)\bMusic"
composer_pattern = r"Music(?:\s*\([^)]+\))*.*?(?:attributed to|by)\s+([^\n\d]*)"
writer_pattern = r"Text(?:\s*\([^)]+\))*.*?(?:attributed to|by)\s+([^\n\d]*)"
venue_pattern = r"Performed at\s*([^\n\d]+)(?:\bSEASON:)"
date_pattern = r"SORTING DATE:\s*(\d{4}-\d{1,2}-\d{1,2})"

results = []

# Uses regex patterns to extract all relevant data
for entry in entries:
    data = {
        "title": clean(re.search(title_pattern, entry).group(1) if re.search(title_pattern, entry) else None),
        "composer": clean(re.search(composer_pattern, entry).group(1) if re.search(composer_pattern, entry) else None),
        "writer": clean(re.search(writer_pattern, entry).group(1) if re.search(writer_pattern, entry) else None),
        "venue": clean(re.search(venue_pattern, entry).group(1) if re.search(venue_pattern, entry) else None),
        "sorting_date": re.search(date_pattern, entry).group(1) if re.search(date_pattern, entry) else None
    }

    results.append(data)

with open("venice_data.json", "w") as file:
    json.dump(results, file, indent=2)
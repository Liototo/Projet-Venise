import re

with open("text.txt", "r") as file:
    text = file.read()

def clean(s):
    if not s:
        return None
    # remove trailing digits, punctuation, or symbols (* † ‡)
    s = re.sub(r"[\d\*\†\‡\s\.,;:]+$", "", s.strip())
    return s.strip()

title_pattern = r"(?m)^(.*?)\n\[[^\n]+\]\s*$"
composer_pattern = r"Music(?:\s*\([^\)]*\))?\s*(?:attributed to|by)\s+([^\n\d]+)"
writer_pattern = r"Text(?:\s*\([^\)]*\))?\s*(?:attributed to|by)\s+([^\n\d]+)"
venue_pattern = r"Performed at\s*([^\n\d]+)"
date_pattern = r"SORTING DATE:\s*(\d{4}-\d{1,2}-\d{1,2})"

data = {
    "title": clean(re.search(title_pattern, text).group(1) if re.search(title_pattern, text) else None),
    "composer": clean(re.search(composer_pattern, text).group(1) if re.search(composer_pattern, text) else None),
    "writer": clean(re.search(writer_pattern, text).group(1) if re.search(writer_pattern, text) else None),
    "venue": clean(re.search(venue_pattern, text).group(1) if re.search(venue_pattern, text) else None),
    "sorting_date": re.search(date_pattern, text).group(1) if re.search(date_pattern, text) else None,
}

print(data)
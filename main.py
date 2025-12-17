import re
import spacy
import json
from collections import defaultdict

# Removes undesired characters often found at the beginning/end of lines in our OCR scan
def clean(s):
    if not s:
        return None
    s = re.sub(r"[\d\*\s\.,;:\"'?!>\(]+$", "", s.strip())
    s = re.sub(r"TM+$", "", s)
    return s.strip()

with open("text_clean.txt", "r") as file:
    text = file.read()

# Splits file into entries (every final line in an entry begins with "Listed as", so we use that as separator)
entries = re.split(r"(?m)^\s*Listed as*s", text)
entries = [e.strip() for e in entries if e.strip()]
entries.pop()

# Load NER model
nlp = spacy.load("en_core_web_sm")

# Regex patterns used to extract data
title_pattern = r"(?m)^(?:\d{4}/\d{1,2}\s+)?(.+?)\bMusic"
composer_pattern = r"Music(?:\s*\([^)]+\))*.*?(?:by|attributed to|attrib. to|adapted from)\s+([^\n\d]*)"
writer_pattern = r"(?:Text|Libretto)(?:\s*\([^)]+\))*.*?(?:attrib. to|attributed to|by|derived from|revised from|adapted by|adapted from|adapted anonymously from|possibly adapted from)\s+([^\n\d]*)"
venue_pattern = r"(?:Performed|Given|Opened) at\s*([^\n\d]+)(?:\bSEASON:)"
date_pattern = r"SORTING DATE:\s*(\d{4}-\d{1,2}-\d{1,2})"

re_results = []
named_entities = defaultdict(list)

opera_id = 0

# Uses regex patterns + NER to extract all relevant data
for entry in entries:

    opera_id += 1

    data = {
        "uid": opera_id,
        "title": clean(re.search(title_pattern, entry, re.IGNORECASE).group(1) if re.search(title_pattern, entry) else None),
        "composer": clean(re.search(composer_pattern, entry, re.IGNORECASE).group(1) if re.search(composer_pattern, entry) else None),
        "writer": clean(re.search(writer_pattern, entry, re.IGNORECASE).group(1) if re.search(writer_pattern, entry) else None),
        "venue": clean(re.search(venue_pattern, entry, re.IGNORECASE).group(1) if re.search(venue_pattern, entry) else None),
        "sorting_date": re.search(date_pattern, entry, re.IGNORECASE).group(1) if re.search(date_pattern, entry) else None
    }

    re_results.append(data)

    doc = nlp(entry)

    for ent in doc.ents:
        if ent.label_ in ["PERSON", "GPE", "LOC"]:
            occurrence = {
                "uid": opera_id,
                "context": re.sub("\n", " ", ent.sent.text)
            }
            named_entities[ent.text].append(occurrence)

# Write data in JSON files
with open("venice_data.json", "w") as file:
    json.dump(re_results, file, indent=2)
with open("ner_results.json", "w") as file:
    json.dump(named_entities, file, indent=2)
import json
from ner_cleanup import undesired_entities, entity_synonyms

with open("ner_results.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Merge "entity synonyms", e.g. occurences of "Vivaldi" and "Antonio Vivaldi"
for target, keys in entity_synonyms.items():
    combined = []
    for k in keys:
        if k in data:
            combined.extend(data[k])
            del data[k]
    data[target] = data.get(target, []) + combined

# Remove undesired entities
data = {k: v for k, v in data.items() if k not in undesired_entities}

# Sort entities by number of occurences; only keeps the 100 most frequent 
occurrences = (sorted(data.items(), key=lambda item: len(item[1]), reverse=True))[:100]

with open("entity_occurrences.json", "w", encoding="utf-8") as file:
    json.dump(occurrences, file, indent=2)
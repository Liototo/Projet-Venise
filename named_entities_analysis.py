import json
from ner_cleanup import undesired_entities

with open("ner_results.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for key in data:
    data[key] = list(dict.fromkeys(data[key]))

data = {k: v for k, v in data.items() if k not in undesired_entities}

occurrences = (sorted(data.items(), key=lambda item: len(item[1]), reverse=True))[:100]

with open("entity_occurrences.json", "w", encoding="utf-8") as file:
    json.dump(occurrences, file, indent=2)
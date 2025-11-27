import spacy
import json

print('Loading NER model...')

nlp = spacy.load("en_core_web_sm")

print('Done!\n')

print ('Doing the complicated work...')

with open("demo_text.txt", "r") as file:
    demo_text = file.read()

doc = nlp(demo_text)
results = []

for ent in doc.ents:
    if ent.label_ in ["PERSON", "GPE", "LOC", "DATE"]:
        results.append({
            "text": ent.text,
            "label": ent.label_,
            "context": ent.sent.text
        })

print(f'Done! {len(results)} entities found\n')

print('Writing to file...')

with open("ner_results.json", "w") as file:
    json.dump(results, file, indent=2)

print('Done! Open ner_results.json for results')
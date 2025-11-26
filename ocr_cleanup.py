import unicodedata
import re

with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = unicodedata.normalize("NFKD", text)
text = re.sub(r"’", "'", text)
text = re.sub(r"[^\x00-\x7F]+", "", text)

with open("text_clean.txt", "w") as file:
    file.write(text)
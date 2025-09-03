import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Barack Obama was the 44th President of the United States.")

displacy.serve(doc, style="ent")
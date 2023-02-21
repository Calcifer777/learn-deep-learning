# %%
import spacy
# %%

nlp = spacy.load("en_core_web_md")

# %%
text = "the customer number for miss Ann is 33012552"
doc = nlp(text)

# %%
spacy.displacy.render(doc, style="ent")

# %%
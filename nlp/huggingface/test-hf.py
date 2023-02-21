# %%
from datasets import Dataset
from transformers import AutoTokenizer

# %%

checkpoint = "bert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(checkpoint)

# %%

s = """
The floods have killed nearly 1,000 people across Pakistan since June, while thousands have been displaced - and millions more affected.
As the BBC drove through Sindh, there were displaced people in every village.
The full scale of the devastation in the province is yet to be fully understood - but the people described it as the worst disaster they've survived.
Floods are not uncommon in Pakistan, but people here said these rains were different - more than anything that's ever been seen. One local official called them "floods of biblical proportions". 
"""
tokens = tokenizer(s)
# %%

data = {"text": [s]}

# %%

def tokenize_function(d):
  return tokenizer(d['text'], truncation=True)


ds = (
  Dataset.from_dict(data)
)
ds_tkn = ds.map(tokenize_function, batched=True)


# %%
from transformers import DataCollatorWithPadding

data_collator = DataCollatorWithPadding(
  tokenizer=tokenizer, 
  return_tensors="tf"
)

tf_dataset = ds_tkn.to_tf_dataset(
    columns=["input_ids", "token_type_ids", "attention_mask"],
    label_cols=["labels"],
    batch_size=2,
    collate_fn=data_collator,
    shuffle=True
)

# %%

# batch = data_collator([s])
# %%

# %%

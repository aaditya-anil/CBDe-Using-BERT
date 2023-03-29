import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("Narrativaai/deberta-v3-small-finetuned-hate_speech18", use_fast=False)

model = AutoModelForSequenceClassification.from_pretrained("Narrativaai/deberta-v3-small-finetuned-hate_speech18")

# Get the text
print("\n\n\n\n\n")
text = input("enter text: ")
# Encode the text into a tensor
input_ids = torch.tensor(tokenizer.encode(text)).unsqueeze(0)  # Batch size 1

# Generate output
with torch.no_grad():
    output = model(input_ids)

# Get the logits for the last hidden state
logits = output[0][0]

# Apply a sigmoid function to get probabilities
probs = torch.sigmoid(logits)

# Get the probability of hate speech
hate_prob = probs[1].item()

# Determine the label
if hate_prob >= 0.5:
    label = "Hate"
else:
    label = "No hate"



print("Hate probability:", hate_prob)
print("Label:", label)

#working Python BERT --

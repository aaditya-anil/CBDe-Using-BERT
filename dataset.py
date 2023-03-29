from datasets import load_dataset

dataset = load_dataset("hate_speech18")
for data in dataset["train"][:100]:
    print(data["text"])


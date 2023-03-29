from flask import Flask, render_template, request
from googleapiclient.discovery import build
import json
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification


app = Flask(__name__)

app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      if request.form['button'] == 'YouTube':
        result = request.form
        hatecomments = commentretrieve(result["urlid"])
        return render_template("result.html",result = hatecomments)

def commentretrieve(videoid):
    hatecomments = {'test':'test'}
    # API Key
    api_key = "AIzaSyBYdvFq336sT16dwyq3Zx6MhgsyLea8VVQ"

    # YouTube video ID
    video_id = videoid

    # Initialize the YouTube API client
    youtube = build("youtube", "v3", developerKey=api_key)

    # Call the YouTube API to retrieve comments for the specified video
    result = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        textFormat="plainText"
    ).execute()

    # Loop through the comments and print each comment along with the author's channel ID
    for item in result["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        author_id = item["snippet"]["topLevelComment"]["snippet"]["authorChannelId"]["value"]
        prediction, probabilty = hateornohate(comment)
        probabilty = probabilty * 100

        if (prediction == 'Hate'):
            hatecomments[comment] = author_id 

        print(f"Comment: {comment}\nAuthor Channel ID: {author_id}\nPrediction: {prediction}\nHate Probabilty: {round(probabilty,2)}% \n\n")
    
    return hatecomments

def hateornohate(comment):

    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained("Narrativaai/deberta-v3-small-finetuned-hate_speech18", use_fast=False)
    model = AutoModelForSequenceClassification.from_pretrained("Narrativaai/deberta-v3-small-finetuned-hate_speech18")

    # Get the text
    print("\n\n\n\n\n")
    text = comment

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

    return label, hate_prob

    print("Text:",text)
    print("Hate probability:", hate_prob)
    print("Label:", label)

    #working Python BERT --

##EOF

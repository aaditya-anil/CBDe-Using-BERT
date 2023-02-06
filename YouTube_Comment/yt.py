from googleapiclient.discovery import build
import json

# API Key
api_key = "AIzaSyBYdvFq336sT16dwyq3Zx6MhgsyLea8VVQ"

# YouTube video ID
video_id = "aT6xCto_sak"

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
    print(f"Comment: {comment}\nAuthor Channel ID: {author_id}\n")

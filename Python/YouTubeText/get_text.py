# importing modules
from youtube_transcript_api import YouTubeTranscriptApi

# using the srt variable with the list of dictionaries
# obtained by the .get_transcript() function
srt = YouTubeTranscriptApi.get_transcript("TyuGBi6joxY")

picked_lines = []
for line in srt:
    text = line["text"]
    picked_lines.append(text.strip().replace("\n", ""))

# print(picked_lines)
with open("subtitles.txt", "w") as f:
    f.write(" ".join(picked_lines))

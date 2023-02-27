from webserver import keep_alive
import requests

channelID = 1003413720417964114
headers = {
    "authorization":
    "MTAwMzQxOTI0MTg2MjY3NjUyMg.G-Rasa.gy4uedWxxYMVMMPnOeegGDiE_LKeTnnmLLSwBA"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})

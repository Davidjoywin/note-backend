import json
import requests

with open("credential.json", 'r') as file:
    _credential = json.loads(file.read())

webhook_url = _credential['webhook_url']

def sendMessage(content):
    req = requests.post(url=webhook_url, data={"content": content})
    print(req.raise_for_status)

def createNote(user, topic):
    message = f"{user} -> Created: {topic}"
    sendMessage(message)

def readNote(user, topic):
    message = f"{user} -> Read: {topic}"
    sendMessage(message)


def updateNote(user, topic):
    former, new = topic.values()

    if former == new:
        message = f"{user} -> Updated: {former}"
    else:
        message = f"{user} -> Updated from '{former}' to {new}"
    sendMessage(message)

def deleteNote(user, topic):
    message = f"{user} -> Deleted: {topic}"
    sendMessage(message)

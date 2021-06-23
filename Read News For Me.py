import requests
import json

r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=d8a7a2541da04e5bb6ea0fa31f26d2db")
data = r.text
parsed = json.loads(data)


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == "__main__":
    for i in range(10):
        str = (parsed['articles'][i]['title'])
        speak(f"Headline number {i + 1}")
        # speak(parsed['articles'][i]['description'])
        speak(str)

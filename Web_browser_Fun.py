import webbrowser
import time
import random

while True:
    websites = random.choice(['https://www.google.com/', 'www.youtube.com/c/TamilCloudguy'])
    webbrowser.open(websites)
    seconds = random.randrange(1, 5)
    time.sleep(seconds)

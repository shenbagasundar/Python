import requests


def NewsFromBBC():
    url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=<Your API Key>"

    # fetching data in json format
    open = requests.get(url).json()

    # getting all articles in a string article
    article = open["articles"]

    # empty list which will contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])


if __name__ == '__main__':
    NewsFromBBC()

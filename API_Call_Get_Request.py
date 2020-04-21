import requests

def NewsFromBBC():
    # BBC news api
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=ef34daa80be44877a3ec97f26d8183f1"

    # fetching data in json format
    open_bbc_page = requests.get(main_url).json()

    # getting all articles in a string article
    article = open_bbc_page["articles"]

    # empty list which will
    # contain all trending news
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):
        # printing all trending news
        print(i + 1, results[i])

    # Driver Code


if __name__ == '__main__':
    # function call
    NewsFromBBC()

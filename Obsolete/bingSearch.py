import requests
import json

#question = " What word does NestlÃ© use to describe their Toll House chocolate chips?"
def searching(question):

    sub_key = "befb9aa5764b4f70804918b476383818"
    assert sub_key

    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    search_term = question

    headers = {"Ocp-Apim-Subscription-Key" : sub_key}
    params  = {"q": search_term, "textDecorations":True, "textFormat":"HTML"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()

    search_results = response.json()

    search_results = search_results["webPages"]["value"]

    searchString = json.dumps(search_results)
    #print(type(searchString))
    #print(searchString)
    return searchString

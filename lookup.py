import googleSearcher2
import search

def run(redQuestion,answers):
    result = googleSearcher2.searching(redQuestion)

    countRes = [-1,-1,-1]

    for i in range(0,3):
        countRes[i] = search.count_occurrences(answers[i].lower(),result)
        #countRes[i] = search.count_occurrences("morsel",result)

    return countRes

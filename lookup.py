import googleSearcher2
import search
#import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize

def run(redQuestion,answers):
    """first run - searches the question and finds the answer"""
    result = googleSearcher2.searching(redQuestion)

    countRes = [-1,-1,-1]

    for i in range(0,3):
        countRes[i] = search.count_occurrences(answers[i].lower(),result.lower())

    """second run - searches each of the answers and finds key words in the question"""
    if countRes == [0,0,0]:
        keywords = word_tokenize(redQuestion)
        proper_nouns = []
        nouns = []
        keywords = pos_tag(keywords)
        for word in keywords:
            if word[1] == 'NN' or word[1] == 'NNS':
                nouns.append(word[0])
            if word[1] == 'NNP' or word[1] == 'NNPS':
                proper_nouns.append(word[0])

        print(countRes,"\n\n\n\n")

        print(nouns)
        print(proper_nouns)
        #now search answers
        for i in range(0,3):
            ansRes = googleSearcher2.searching(answers[i])
            for j in nouns:
                countRes[i] += search.count_occurrences(j.lower(),ansRes.lower())
            print(countRes)
            for j in proper_nouns:
                countRes[i] += search.count_occurrences(j.lower(),ansRes.lower())
            print(countRes)

    return countRes

#print(run("PBS icon named honorary captain National Hockey League team?",["Mister Rogers","Bob Ross","William F. Buckley Jr."]))

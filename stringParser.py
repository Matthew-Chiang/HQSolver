#str = "What word does NestlÃ© use \r\nto describe their Toll House \r\nchocolate chips? \r\nMorsels \r\nNibbles \r\nSamples \r\n"

def strPrsr(prompt):
    listTotal = list(s.strip() for s in prompt.splitlines())

    listTotal = list(filter(None, listTotal))

    answersList = listTotal[-3:]

    questionList = listTotal[:-3]

    question = ""
    for i in range(len(questionList)):
        question += questionList[i]
        question += " "

    #print(answersList)
    #print(question)

    return question,answersList

#print(strPrsr(str))

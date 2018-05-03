
def parse(question):
    splitQuestion = question.split(" ")

    #if the question starts with which add the names at the back
    '''if splitQuestion[0] == 'Which' or splitQuestion[0] == 'What':
        question += " "
        question += ans[0]
        question += " "
        question += ans[1]
        question += " "
        question += ans[2]'''

    # replace & with and
    question = question.replace("&","and")

    #remove bad words
    question = question.replace(" and "," ")
    question = question.replace(" of "," ")
    question = question.replace(" the "," ")
    question = question.replace(" would "," ")
    question = question.replace(" which "," ")
    question = question.replace(" what "," ")
    question = question.replace(" for "," ")
    question = question.replace(" was "," ")
    question = question.replace(" a "," ")
    question = question.replace(" an "," ")
    question = question.replace(" does "," ")
    question = question.replace(" at "," ")
    question = question.replace(" in "," ")
    question = question.replace(" it "," ")
    question = question.replace(" its ", " ")


    question = question.replace("Which "," ")
    question = question.replace("What "," ")
    question = question.replace("An "," ")
    question = question.replace("A "," ")


    keywords = question.replace("?","")
    keywords = question.replace(",","")

    return question

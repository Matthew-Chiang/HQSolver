import csv

def save(question,ans, RQuestion):
    print(question)
    print(type(question))
    Row = [question,RQuestion]
    Row = Row + ans
    with open("Results/QA.csv",'a',encoding='utf-8') as fd:
        fileWriter = csv.writer(fd,lineterminator='\n')
        fileWriter.writerow(Row)

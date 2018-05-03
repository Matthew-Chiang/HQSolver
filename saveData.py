import csv

def save(question,ans, RQuestion,predicted):
    print(question)
    Row = [question,RQuestion]
    Row = Row + ans
    Row.append(predicted)
    with open("Results/QA2.csv",'a',encoding='utf-8') as fd:
        fileWriter = csv.writer(fd,lineterminator='\n')
        fileWriter.writerow(Row)

#import picTaker  #takes the screenshot when imported
import stringParser
import googleSearcher2
import search
import ocr
import questionParser
import saveData

#testing functions
import time
#start = time.time()
#import picTaker
#end = time.time()
#print(end - start , "picTaker")

masterStart = time.time()
start = time.time()
wordPic = ocr.getStr("Results/Pics/2018-04-18/3PM/5.png")
#wordPic = ocr.getStr("Screenshots/exampleProduction.png")
#print(wordPic)
end = time.time()
print(end-start,"wordPic")
#print(wordPic)
start = time.time()
(question,answers) = stringParser.strPrsr(wordPic)
end = time.time()
print(end-start,"string Parser")
print("\n\n",question)
print(answers,"\n\n")

redQuestion = questionParser.parse(question)

saveData.save(question,answers,redQuestion)

start = time.time()
result = googleSearcher2.searching(redQuestion)
end = time.time()
print(end-start,"google Searcher")


countRes = [-1,-1,-1]

start = time.time()
for i in range(0,3):
    countRes[i] = search.count_occurrences(answers[i].lower(),result)
    #countRes[i] = search.count_occurrences("morsel",result)
end = time.time()
print(end-start,"searching\n")

print(countRes)

ansNum = []
ansVal = max(countRes)
count = 0
for key,val in enumerate(countRes):
    if val == ansVal:
        ansNum.append(key)
        count += 1

masterEnd = time.time()
print("\n",masterEnd-masterStart, "  total\n")

totSum = sum(countRes)
if totSum == 0:
    print("I DONT KNOW")
else:
    if count == 1:
        print(answers[ansNum[0]])
        print(countRes[ansNum[0]]/sum(countRes)*100)
    else:
        print("TIE")
        for key,val in enumerate(ansNum):
            print(answers[ansNum[key]],"\n",)

import picTaker  #takes the screenshot when imported
import stringParser
import ocr
import questionParser
import saveData
import lookup

#testing functions
import time
#start = time.time()
#import picTaker
#end = time.time()
#print(end - start , "picTaker")

masterStart = time.time()
#wordPic = ocr.getStr("Results/Pics/2018-04-18/3PM/9.png")
wordPic = ocr.getStr("Screenshots/exampleProduction.png")
#print(wordPic)
#print(wordPic)
(question,answers) = stringParser.strPrsr(wordPic)

print("\n\n",question)
print(answers,"\n\n")

redQuestion = questionParser.parse(question)

countRes = lookup.run(redQuestion,answers)

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
ans_str = ""
if totSum == 0:
    ans_str += "I DONT KNOW"
    print(ans_str)
else:
    if count == 1:
        ans_str += str(answers[ansNum[0]])
        print(ans_str)
        print(countRes[ansNum[0]]/sum(countRes)*100)
    else:
        ans_str += "TIE"

        for key,val in enumerate(ansNum):
            ans_str += str(answers[ansNum[key]])
        print(ans_str)

saveData.save(question,answers,redQuestion,ans_str)

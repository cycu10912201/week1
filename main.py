
print("輸入五次數字，計算平均值")
from myMath import myStatistics as F

A=[]

for i in range(1,6):
    print("第",i,"次")
    A.append(float(input()))

print("平均值為",F.myMean(A))

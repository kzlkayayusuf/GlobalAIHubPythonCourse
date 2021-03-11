
"""
Created on Thu Mar 11 12:55:41 2021

@author: kzlkayayusuf
"""

oddNumbersList = list(range(1,10,2))
evenNumbersList = list(range(0,11,2))
oddNumbersList.extend(evenNumbersList)
oddNumbersList.sort()


newList=[]

for i in oddNumbersList:
    number = oddNumbersList[i]*2
    newList.append(number)
    print(f"Yeni listenin {i}.inci elemanı {newList[i]}'nin türü: {type(newList[i])}")
    


import math


def get_pairs(list):
  list.sort()
  count= 1
  for i in list :
    comp = list[i]
    if (comp== list[i+1]):
        print("----",comp)
        count= count+1      
  count= count/2 
  round = math.floor(count)
  print(round)  

get_pairs([1,1,2,2,1,2,6])
#get_pairs([9,10,20,20,10,10,30,50,10,20])
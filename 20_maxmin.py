import math


def get_max(list):
  list.sort()
  min= list[0]+list[1]+list[2]+list[3]
  max= list[-1]+list[-2]+list[-3]+list[-4]
  #tam= len(list)

    
  print(min,max)

get_max([1,3,5,7,9])
get_max([1,2,3,4,5])
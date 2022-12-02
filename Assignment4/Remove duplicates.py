lst = [1,2,2,3,4,5]

dic = {}
for i in set(lst):
    dic[i] = lst.count(i)
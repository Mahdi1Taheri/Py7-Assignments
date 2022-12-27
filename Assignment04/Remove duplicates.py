lst = [1,2,2,3,7,7,5]

dic = {}
for i in set(lst):
    dic[i] = lst.count(i)
    if dic[i] > 1:
        lst.remove(i)

print(lst)

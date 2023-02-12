input_list=[1,1,2,3,3,4,5,6,6]
b=set(input_list)
s=[]
for i in b:
    if input_list.count(i)>1:
        s.append(i)
print(s)

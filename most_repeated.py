input_list=[1,2,4,3,2,4,2,5,7,2]
b=set(input_list)
s={}
for i in b:
    s[i]=input_list.count(i)
max_frequency=0
most_frequent_element = None
for element, frequency in s.items():
    if frequency > max_frequency:
        max_frequency = frequency
        most_frequent_element = element
print("high frequency number is:",most_frequent_element)
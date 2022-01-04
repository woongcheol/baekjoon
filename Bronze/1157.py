a = input().upper()
a_list = list(set(a))

a_count = []
for i in a_list:
    count = a.count(i)
    a_count.append(count)

if a_count.count(max(a_count)) > 1:
    print("?")
else:
    maxCount = a_count.index(max(a_count))
    print(a_list[maxCount])
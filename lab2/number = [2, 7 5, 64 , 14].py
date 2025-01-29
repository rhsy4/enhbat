count = 0
number = [2, 7,5, 64 , 14]
odd = []
even = []
for i in number:
    if i % 2 == 0:
        count += 1
        even.append(i)
    else:
        count += 1
        odd.append(i)
print("The total number of even numbers are:", len(even))
print("The total number of odd numbers are:", len(odd))
print("The odd numbers are:", odd)
print("The even numbers are:", even)

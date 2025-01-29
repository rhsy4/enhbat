numbers = [2, 7, 5, 64, 14]
even_numbers = []
index = 0
while index < len(numbers):
    if numbers[index] % 2 == 0: 
        even_numbers.append(numbers[index])
    index += 1
print("Output:", even_numbers)

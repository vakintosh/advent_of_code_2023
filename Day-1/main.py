with open("input.txt", "r") as trebuchet:
    lines = trebuchet.readlines()
    lines = [line.strip() for line in lines]
    
number = []


for i in lines:
	total = 0
	num = [int(s) for s in i if s.isdigit()]
	first_num= str(num[0])
	last_num = str(num[-1])
	numbers = int(first_num + last_num)
	number.append(numbers)
print(number)

sum_number = sum(number)

print(sum_number)
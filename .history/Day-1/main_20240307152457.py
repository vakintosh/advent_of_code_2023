# with open("input.txt", "r") as trebuchet:
# 	lines = trebuchet.readlines()
# 	print(lines)
#  
with open("input.txt", "r") as trebuchet:
    lines = trebuchet.readlines()
    lines = [line.strip() for line in lines]

for i in lines:
	total = 0
	number= []
	num = [int(s) for s in i if s.isdigit()]
	first_num= str(num[0])
	last_num = str(num[-1])
	numbers = int(first_num + last_num)
	print(numbers)
	total += numbers
	print(total)

	# print("The sum is :", numbers)



# with open("input.txt", "r") as trebuchet:
# 	lines = trebuchet.readlines()
# 	print(lines)
#  
with open("input.txt", "r") as trebuchet:
    lines = trebuchet.readlines()
    lines = [line.strip() for line in lines]

for i in lines:
	total = 0
	num = [int(s) for s in i if s.isdigit()]
	first_num= int(num[0])
	last_num = int(num[-1])
	number = list(first_num + last_num)
	for num in number:
		total += num
 
print("The sum is :", total)



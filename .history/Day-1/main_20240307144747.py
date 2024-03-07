# with open("input.txt", "r") as trebuchet:
# 	lines = trebuchet.readlines()
# 	print(lines)
#  
with open("input.txt", "r") as trebuchet:
    lines = trebuchet.readlines()
    lines = [line.strip() for line in lines]

for i in lines:
    # print (i)
	num = [int(s) for s in i if s.isdigit()]
	first_num= num[0]
	last_num = num[-1]
	number = first_num + last_num
	print(number)



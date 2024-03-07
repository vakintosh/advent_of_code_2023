# with open("input.txt", "r") as trebuchet:
# 	lines = trebuchet.readlines()
# 	print(lines)
#  
with open("input.txt", "r") as trebuchet:
    lines = trebuchet.readlines()
    lines = [line.strip() for line in lines]
    # num = [int(s) for s in line.split() if s.isdigit()]

for i in lines:
    # print (i)
	num = [int(s) for s in i.split() if s.isdigit()]
	print(num)
# print(lines)


# with open("input.txt", "r") as trebuchet:
# 	lines = trebuchet.readlines()
# 	print(lines)
 
with open("input.txt", "r") as trebuchet:
    lines = trebuchet.readlines()
    lines = [line.strip() for line in lines]
    num = [int(s) for s in lines.split() if s.isdigit()]

print(lines)


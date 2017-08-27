score = float(input(":"))

if score >= 60:
	grade = -(score//10) + 74
else:
	grade = 69

print(chr(int(grade)))
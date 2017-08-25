import random

number = random.randint(0,10)

print ("\n 	这是一个 0-10 间的整数，你有3次猜测机会")

for i in range(0,3):

	guess = int(input ("\n  请输入你猜的数字："))


	if guess == number:
		print ("\n 	恭喜你，猜对了")
		break
	else:
		if guess > number:
			if 2-i >0:
				print ("\n 	猜大了，你还有%d次机会\n"%(2-i))
			else:
				print ("\n 	没有机会了，游戏结束")
		else:
			if 2-i >0:
				print ("\n 	猜小了，你还有%d次机会\n"%(2-i))
			else:
				print ("\n 	没有机会了，游戏结束")
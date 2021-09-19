import random

b=[
	0,1,2,
	3,4,5,
	6,7,8
]

def show():
	print(b[0],"|",b[1],"|",b[2])
	print("--------")
	print(b[3],"|",b[4],"|",b[5])
	print("--------")
	print(b[6],"|",b[7],"|",b[8])

show()

def User_input():
	user_ip=int(input("Choose YOUR position: "))
	if b[user_ip]!='x' and b[user_ip]!='o':
		b[user_ip]='x'
	else:
		print("Position NOT available.Try another position.")
		User_input()


def Comp_input():
	comp_ip=random.randint(0,8)
	if b[comp_ip]!='o' and b[comp_ip]!='x':
		b[comp_ip]='o'
	else:
		Comp_input()

def win(str):
	if b[0]==str and b[1]==str and b[2]==str:
		return True
	elif b[3]==str and b[4]==str and b[5]==str:
		return True
	elif b[6]==str and b[7]==str and b[8]==str:
		return True
	elif b[0]==str and b[4]==str and b[8]==str:
		return True
	elif b[2]==str and b[4]==str and b[6]==str:
		return True
	elif b[0]==str and b[3]==str and b[6]==str:
		return True
	elif b[1]==str and b[4]==str and b[7]==str:
		return True
	elif b[2]==str and b[5]==str and b[8]==str:
		return True


while True:
	if win('x') is True:
		print("Player X Won.")
		break
	elif win('o') is True:
		print("Player O Won.")
		break
	else:
		User_input()
		Comp_input()
		show()






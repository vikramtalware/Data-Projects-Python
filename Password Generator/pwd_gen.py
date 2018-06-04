import string, random, sys

def pwd_gen():
	a = input('What should be the length of your password: ')
	chars=string.ascii_letters + string.digits + string.punctuation
	try:
		while int(a) < 8:
			b = input('We encourage you to enter a number >= 8 for strong passwords. Do you agree (Y/N): ').upper()
			if (b == 'N'):
				file = open("words.txt",'r')
				file.seek(0)
				content = file.readlines()
				content = [i.strip("\n") for i in content if len(i)==int(a)+1]
				j = random.randint(0,len(content))
				print ("Here's your weak password: "+content[j])
				sys.exit(1);
			elif (b == 'Y'):
				c = input('What should be the length of your strong password: ')
				if (int(c) >= 8):
					print ("Here's your strong password: "+''.join(random.choice(chars) for i in range(int(c))))
					sys.exit(1);
				else:
					print('Sorry, Try Again!')
			else:
				print('Sorry, Try Again!')
		print ("Here's your password "+''.join(random.choice(chars) for i in range(int(a))))
	except ValueError:
		print('Please make sure you have entered a number.')
		return pwd_gen()
pwd_gen()

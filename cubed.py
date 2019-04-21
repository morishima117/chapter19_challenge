def number(num):
	try:
		num=int(num)
		num=num**3
		print(num)
	except ValueError:
		print('数値を入力')




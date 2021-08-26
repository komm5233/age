driving = input('請問有沒有開過車?')
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('通過')
	else:
		print('你沒駕照阿')
elif driving == '沒有':
	if age < 18:
		print('很好，過幾年就可以考了')
	else:
		print('你他媽能去考了')		
else:
	print('請輸入有或沒有')
	
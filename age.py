driving = input('開過車嗎?')
if driving != 'yes' and driving != 'no':
    print('只能輸入 yes / no')
    raise SystemExit
age = input('你幾歲?')
age = int(age)
if driving == 'yes':
	if age >= 18 :
		print('ok')
	else:
		print('oh')
elif driving == 'no':
	if age >= 18 :
		print('可考')
	else:
		print('ooo')

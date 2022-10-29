driving = input ('請問您有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input ('請問您的年齡? ')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜!您通過測驗了')
	else:
		print('奇怪!您怎能開車。')
elif driving == '沒有':
	if age >= 18:
		print('您該去考駕照了')
	else:
		print('等你年滿18歲再去考駕照')
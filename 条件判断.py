h = float(input('输入您的身高（米）：'))
w = float(input('输入您的体重（千克）: '))
bmi = w/(h * h)
print('bmi is %s' % bmi)
if bmi < 18.5:
    print('guoqin')
elif bmi < 25:
    print('zhengchang')
elif bmi < 28:
    print('guozhong')
elif bmi < 32:
    print('feipang')
else:
    print('yanzhengfeipang')
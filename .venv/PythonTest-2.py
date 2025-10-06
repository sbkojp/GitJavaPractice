# score = int(input('点数を入力'))
# if score >=40:
#     print('合格')
# else:
#     print('追試')

date=[[1,2,3],
      [4,5,6],
      [7,8,9]]
print(date)

number=1+2+3 \
+4+5+6 \
+7+8+9
print(number)

number=1+2+3 \
       +4+5+6 \
       +7+8+9
print(number)

apple = 250
n = 3
print(apple * n)

answer = 5 * ((5+1)/2)
print(answer)

a=3
b=4
a **= b
print(a)
a //=b
print(a)
a //=b
print(a)

answer = 0.1+0.1+0.1
print(answer)

print(round(2.5),round(2.4),round(2.6))
def half_up_round(number):
    """一般的な四捨五入(.5を切り上げる)
    を行う関数
    """
    return int(number + 0.5)

print(f"2.4の四捨五入:{half_up_round(2.4)}")

from decimal import Decimal,ROUND_HALF_UP
# Decimal型に変換（正確な計算の為）
num_2_5 = Decimal('2.5')
num_2_4 = Decimal('2.4')
num_2_6 = Decimal('2.6')
# 指定した桁数でROUND_HALF_UPルールを適用
# '0'は「小数点第一位で四捨五入して整数にする」
print(num_2_5)
print(type(num_2_4))
print(type(num_2_6))

result_2_5=num_2_5.quantize(Decimal('0'),rounding=ROUND_HALF_UP)
result_2_4=num_2_4.quantize(Decimal('0'),rounding=ROUND_HALF_UP)
result_2_6=num_2_6.quantize(Decimal('0'),rounding=ROUND_HALF_UP)

print(f"2.5の四捨五入(Decimal):{result_2_5}")#出力3
print(f"2.4の四捨五入(Decimal):{result_2_4}")#出力2
print(f"2.6の四捨五入(Decimal):{result_2_6}")#出力3

msg='こんにちわ'
msg
msg1="おはよう"
msg1
print(msg)
print(msg1)
msg2='こんにわ\n太郎君'
print(msg2)
msg3='こんにわ\t太郎君'
print(msg3)
msg4='こんにわ\'太郎\'君'
print(msg4)
msg5='こんにわ"太郎"君'
print(msg5)

# m = float(input('長さをメートルで入力＜'))
# cm = m*100
# print(cm)

# 【10/1 P98～】
price =1980
label = str(price) + '円'
print(type(label))
print(label)

# 確認・応用問題　P99
orange = 300
n =  6 
print(orange*n)
orange = 400
n = 5
print(orange*n)

name = '太郎'
message = 'おはよう'
print(name+'くん、'+message)
name = '次郎'
message = 'こんにちわ'
print(name+'さん、'+message)

teihen = 7
jouhen =3
takasa =4
menseki =(jouhen+teihen)*takasa/2
print(type(menseki))
print(menseki)

candy = 100
n = 6
answer = candy // n 
print('ひとり'+str(answer)+'個ずつ')

# 第4章　制御構造
a=5
print(a<10)
print(a>10)
b=0.1+0.1+0.159
c=round(0.1+0.1+0.1,5)
print(b==0.3,c==0.3)

score = int(input('点数を入力　'))
if score >=80:
    print('おめでとう')
    print('合格、成績はAです')
elif score >=60:
    print('頑張りましたね')
    print('合格、成績はBです')
elif score >=40:
    print('次は更に頑張りましょう')
    print('合格、成績はCです')
else:
    print('残念！')
    print('追試')
print('おしまい')

age = int(input('年齢を入力　'))
if age >=10:
    height = int(input('身長を入力　'))
    if height >=140:
        print('乗れる')
    else:
        print('身長制限の為、乗れない')
else:
    print('年齢制限の為、乗れない')


if (age >=10) and (age < 75)and (140 <= height < 190):
    print('乗れる')
else:
    print('乗れない')

key =input('ジェットコースターは好きですか？［Y/N］')
if (key =='Y' or key == 'y'):
    print('明日は遊園地に行く')
elif (key == 'N' or key == 'n'):
    print('明日は動物園に行く')
else:
    print('YかNで答えて下さい')

for i in range(5):
    print(i)

for j in range(1,10):
    print(2*j,end='　')
    print()

for i in range(1,10):
    for j in range(1,10):
        print(i*j,end=' ')
    print()

for i in range(0,50,5):
    print(i,end=' ')
print()

for i in range(10,-20,-1):
    print(i,end=' ')
print()

for i in range(1,10):
    if (i % 3) == 0:
        break
    print(i)
else:
    print('---loop ended---')

for i in range(1,10):
    if i > 3:
        break
    for j in range(1,10):
        if j > 5:
            break
        print(i*j, end=' ')
    print()

for i in range(1,10):
    if(i % 3) ==0:
        continue
    print(i)
else:
    print('---loop ended---')

pin = input('PINを入力')
while (pin != '1234'):
    print('違います')
    pin = input('PINを入力')
print('当たりです')

while True:
    pin = input('PINを入力')
    if (pin == '1234'):
        print('当たりです！')
        break
    else:
        print('違います')

x = int(input('数字を入力'))
if x % 2 == 0:
    print('偶数です')
else:
    print('奇数です')
    
score = 79
if 80<=score<=100:
    print('合格')
else:
    print('不合格')

for i in range(1,6):
    if i==5:
        break
    print(i,end='a')
print(i)


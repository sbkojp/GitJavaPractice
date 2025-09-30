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

m = float(input('長さをメートルで入力＜'))
cm = m*100
print(cm)


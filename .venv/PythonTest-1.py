print("Hello!")
name =input('what is your name?>')
print('Hello! ' + name)
print('bey!'+name)
print('abs(-234) =', abs(-234))
print('sum([1,2,3,4,5]) =', sum([1,2,3,4,5]))
print('ROUND(3.14159, 2) =', round(3.14159, 2) )
print(min(1,2,3,4,5), max(1,2,3,4,5), 
      min('apple', 'banana', 'cherry'), max('apple', 'banana', 'cherry'))
print(len('Hello'), len([1,2,3,4,5]), len((1,2,3,4,5)), len({'a':1, 'b':2, 'c':3}), len({1,2,3,4,5}))
print(int('123'), float('3.14'), str(123), bool(1), bool(0), bool(''))
print(type(123), type(3.14), type('Hello'), type([1,2,3]), type((1,2,3)),
     type({'a':1, 'b':2}), type({1,2,3}))
print(isinstance(123, int), isinstance(3.14, float), isinstance('Hello', str),
     isinstance([1,2,3], list), isinstance((1,2,3), tuple), isinstance({'a':1, 'b':2}, dict), 
     isinstance({1,2,3}, set))
# print(dir([]), dir(()), dir({}), dir(set()), dir(''), dir(123), dir(3.14), 
#       dir(True), dir(False), dir(None))
# print(help([]), help(()), help({}), help(set()), help(''), help(123), help(3.14), 
#       help(True), help(False), help(None))

# print(id(123), id(3.14), id('Hello'), id([1,2,3]), id((1,2,3)), id({'a':1, 'b':2}), 
#       id({1,2,3}), id(True), id(False), id(None))
print(hex(123), hex(255), hex(4095))
print(oct(8), oct(64), oct(512))
print(bin(5), bin(10), bin(255))
print(chr(65), chr(97), chr(48), ord('A'), ord('a'), ord('0'))
print(pow(2,3), pow(3,4), pow(2,10))   
print(divmod(10,3), divmod(20,6), divmod(100,7))
print(round(3.14159), round(3.14159, 2), round(3.14159, 3))
print(format(123456789, ','), format(3.14159, '.2f'), format(3.14159, '.4f'))
print(bin(255), oct(255), hex(255)) 
print(int('11111111', 2), int('377', 8), int('FF', 16))
print(float('3.14'), float('2.718'), float('1.618'))    
print()
print('Hello','Taro','Hanako')
print('Hello' + 'Taro' + 'Hanako')
print('Hello'*3)
print('Hello.'*3,'bey!'*2,sep='-')
print('Hello', 'Taro', sep='-', end='.\n') 
'''P61'''
# v1 = int(input('Enter 1st car is velocity: '))
# v2 = int(input('Enter 2nd car is velocity: '))
# time = int(input('Enter time: '))

# distance = (v1 + v2) * time
# print(distance)

#define = def 

# v1 = int(input('Enter 1st car is velocity: '))
# v2 = int(input('Enter 2nd car is velocity: '))
# time = int(input('Enter time: '))
# def calculateDistance (v1, v2, t):
#     return (v1 + v2) * t

# # d = calculateDistance(70 , 100, 2)
# # print(d)
# print(calculateDistance(70 , 100, 2))



# def calculateDistance (v1, v2, t):
#     return (v1 + v2) * t

# v1 = int(input('Enter 1st car is velocity: '))
# v2 = int(input('Enter 2nd car is velocity: '))
# time = int(input('Enter time: '))

# print(calculateDistance(v1, v2, time))


# def calculateSquare(n):
#     return (n ** 2)
# print(calculateSquare(7))

# def calculateSquare(n):
#     return (n * n)
# print(calculateSquare(7))


# def calcPower(base, exp):
#     return base ** exp
# print(calcPower(3, 4))


# def reverseList(list):
#     return(list [::-1])
# print (reverseList([3, 2, 1]))


#reciprocal

# def calcDevide(n):
#     return (n ** (-1))

# print(calcDevide(5))





# def calc(n, n1):
#     return (n + n1)
# print(calc(5, 6))

# def calc(n, n1, *n2):
#     acc = 0
#     for num in n2:
#         acc += num
#     return n + n1+ acc

# print(calc(2, 3))
        

# def sayHello(name, surname):
#     print(f'Hi, {name}, {surname}')
# # sayHello('Zakir', 'Ikramzhanov')
# sayHello(surname = "Khakimbekov", name = "Elbek")


#slovari
# mentor = {
#     'name': 'Zakir',
#     "suname": 'Ikramzhanov'
#     "ismarried": False
# }

# for key in mentor:
#     print(key, mentor[key])
# print(mentor['age'])
# print(mentor.get('abc'))

# def abc(**args):                   #args
#     acc = 0
#     for key in args:
#         acc += args [key]
#     return acc

# abc(a = 4, b = 6, c = 10)

# def min(a, b):
#     pass

# print(min(10,30))
# print(min(5,10))

# def min(a, b):
#     if a < b:   return a
#     else:   return b

# print(min(10,30))
# print(min(5,10))
# print(min(5,5))

# print(eval('1+4'))             #eval== evaluate вычисли




# def calc(a, b, sign):
#     if sign == 'add': return eval(f'{a} + {b}')
#     if sign == 'substract': return eval(f'{a} - {b}')
#     if sign == 'divide': return eval(f'{a} / {b}')
#     if sign == 'multiply': return eval(f'{a} * {b}')
# print(calc('1', '3', 'add'))
# print(calc('1', '3', 'substract'))
# print(calc('1', '3', 'multiply'))
# print(calc('1', '3', 'divide'))



def calc(a, b, action):
    return eval(f'{a}{signs.get(action){b}')
print(calc('1', '3', 'add'))
print(calc('1', '3', 'substract'))
print(calc('1', '3', 'multiply'))
print(calc('1', '3', 'divide'))
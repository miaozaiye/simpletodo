from django.test import TestCase
import random

# Create your tests here.
# total = 0
# count = 0
#
# while True:
#     line = input('inter:')
#     if line:
#         try:
#             number = int(line)
#         except ValueError as err:
#             print(err)
#             continue
#         total +=number
#         count +=1
#
#     else:
#         break
#
# if count:
#     print('count =',count,'total = ',total,'mean = ',total/count)

zero = [' *** ','*   *','*     *','*     *','*     *','*   *',' *** ']
one = [' *','**',' *',' *',' *',' *','**']
two = [' *** ','*   *','*  *','  *','*  ','*   ','****']
three=['*****','*   *','   * ','  *  ','   * ','*   *','*****']

digit = [zero,one,two,three]

row = 0

inputnumber = input ('pls. input your number(000-333):')

length = len(inputnumber)

# while row <7:
#     column = 0
#     line = ''
#     while column < length:  # 每一行是有 length 个数据的当行*组成的
#
#         digit_line = digit[int(inputnumber[column])]
#         line += digit_line[row]+' '
#         column +=1
#     print(line)
#     row +=1

a = {}
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


# zero = [' *** ','*   *','*    *','*    *','*    *','*   *',' *** ']
# one = [' *','**',' *',' *',' *',' *','**']
# two = [' *** ','*   *','*  *','  *','*  ','*   ','****']
# three=['*****','*   *','   * ','  *  ','    * ','*    *','*****']
#
# digit = [zero,one,two,three]
#
# row = 0
#
# inputnumber = input ('pls. input your number(000-333):')
#
# length = len(inputnumber)
#
# while row <7:
#     column = 0
#     line = ''
#     while column < length:  # 每一行是有 length 个数据的当行*组成的
#         subnum = int(inputnumber[column])
#         digit_row1 = digit[subnum][row]
#         digit_line_count = 0
#         digit_row2 = ''
#         str_num = str(subnum)
#         # print('str_num is:',str_num,' | ','digit_line1[row] is:',digit_row1)
#         while digit_line_count<len(digit_row1):
#             # print(digit_line_count,len(digit_row1))
#             # print('digit_row2 is:',digit_row2,'|','digit_row1[count] is:',digit_row1[digit_line_count])
#             if digit_row1[digit_line_count]== ' ':
#                 digit_row2 +=' '
#             else:
#                 digit_row2 +=str_num
#
#             digit_line_count +=1
#         # print('digit row2 is:',digit_row2,'|','digit row 1 is:',digit_row1)
#         line += digit_row2+'  '
#         column +=1
#     print(line)
#     row +=1




# def awfulpoetry():
#
#     num =['The Boy','The lady','Die Frau','Der Man']
#     act = ['sings','jumped','cries','runs','cooks','reads']
#     adv = ['badly','happpiely','strongly']
#
#     num_len = len(num)
#     act_len = len(act)
#     adv_len = len(adv)
#
#     n = num[random.randint(0,num_len-1)]
#     ac = act[random.randint(0,act_len-1)]
#     ad = adv[random.randint(0,adv_len-1)]
#     sentence = n+' '+ac+' '+ad
#     print (sentence)
#
#     return sentence
#
# line = int(input('pls. input the lines you want to read:'))
#
# for i in range(0,line):
#     awfulpoetry()

dg = []

def datagroup():

    while True:

        data = input('pls. input any number, or press"enter" to close ')

        try:
            dg.append(int(data))
        except ValueError as err:
            break


    # 排序求中位值
    print ('dg is:',dg)
    dg2 =[x for x in range(0,len(dg))]
    dg_sort = []

    for data in range(0,len(dg)):
        count = 0
        print('dg is:' ,dg)
        for data2 in range(0,len(dg)):

            if dg[data]> dg[data2]:
                print (dg[data],' is greater than ',dg[data2])
                count +=1
            else:
                print(dg[data], ' is less than ',dg[data2])
            data2 +=1
        dg_sort+=[[dg[data],count]]
        dg2[count]=dg[data]
        data +=1





    print(dg_sort, dg2)
    sub = len(dg)

    if sub%2:
        mid_num = dg[int((sub-1)/2)]
    else:
        mid_num = (dg[int((sub-1)/2)]+dg[int((sub+1)/2)])/2


    print('numbers:',dg)
    print('count = ',len(dg),' ','sum = ',sum(dg),' ','highest = ', max(dg),' ','mean = ',sum(dg)/len(dg))
    print ('sorted numbers:',dg2,' ','mid-num is:', mid_num)

datagroup()
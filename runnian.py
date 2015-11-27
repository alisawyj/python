#-*- coding:utf-8 -*-
'''判断一个年份是不是闰年'''
'''year = raw_input("please input a year:")
if (int(year)%400 == 0 or (int(year)%4 ==0 and int(year)%4 != 0)):
    print("此年是闰年！！")
else:
    print("不是闰年！！")'''
'''第二种写法'''
'''import time
year = time.localtime()[0]
if year%400 == 0 or year%4 == 0 and year%100 != 0 :
    print "this year %s is leap!!" % year
else:
    print "this is year %s is not leap!!" % year'''
'''找出0~100之间的素数'''
'''import  math
n = 100
flag = []
for i in range(2,n):
    f = True
    for m in range(2,int(math.sqrt(i))+1):
        if i%m == 0:
           f = False
           break
    if f:
        flag.append(i)
for i in range(0,len(flag)):
    print flag[i]
    print "\t\t"'''
'''有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数'''
'''for i in range(1,4):
    for j in range(1,4):
        for k in range(1,4):
            if i!=j and j!=k and i!=k:
                num = i *100 + j *10 + k
                print num'''
'''(2)一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？'''
'''import math
num = 1
while True:
    if math.sqrt(num + 100) - int(math.sqrt(num + 100)) == 0 and math.sqrt(num + 268) - int(math.sqrt(num + 268)) == 0 :
        print num
        break
    else:
        num += 1'''
'''输入三个整数x,y,z，请把这三个数由小到大输出'''
'''l = []
for i in range(1,4):
    num = raw_input("please input a number:")
    l.append(num)
l.sort()
print l'''
'''输入某年某月某日，判断这一天是这一年的第几天？'''
'''months = [0,31,59,90,120,151,181,212,243,273,304,334]
def isleaf(year):
    flag = False
    if (year%400 == 0 or (year%4 == 0 and year%100 != 0)):
        flag = True
    return flag     
def fun(year,month,day):
    if month >= 1 and month <= 12:
        sums = months[month-1]
    else:
        print("error data!!")
    if isleaf(year) and month > 2:
        sums += 1
    sums += day
    print(("%d_%d_%d 是这一年的第%d天")%(year,month,day,sums))
if __name__ == "__main__":
    year = input("please input a bumber:")
    month = input("please input a bumber:")
    day = input("please input a bumber:")
    fun(int(year),int(month),int(day))'''

'''输出9*9口诀'''
'''for i in range(1,10):
    for j in range(1,i+1):
        print(("%d * %d = %d") % (j,i,i*j),end = "   ")
    print("\n")
'''
'''题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？'''
'''a = 1
print("第1个月的兔子总数是%d对" % a)
b = 1
print("第2个月的兔子总数是%d对" % b)
for i in range(3,13):
    c = a + b
    print(("第%d个月的兔子总数是%d对") % (i,c))
    a = b
    b = c'''

'''打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。'''
'''for i in range(100,1000):
    a = int(i / 100)
    b = int(i/10%10)
    c = i % 10
    if a**3 + b**3 + c**3 == i:
        print(i,end = "  ")
        '''
'''将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。'''
'''import math
def isprime(num):
     flag = True
     for i in range(2,int(math.sqrt(num))+1):
          if num%i == 0:
               flag = False
               break
     return flag
def Explode(num):
     print("%d=" % num,end="")
     for i in range(2,int(num/2)+1):
          if isprime(i):
               while num%i == 0:
                    if num/i == 1:
                         print("%d" % i)
                    else:
                         print("%d*" % i,end="")
                    num = num/i
if __name__== "__main__":
     num = input("please input a number:")
     Explode(int(num))'''

                    
'''利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示'''

'''def fun(num):
    if num >= 90:
        print("A")
    elif num >= 60 and num < 90:
        print("B")
    elif num < 60 and num >= 0:
        print("C")
    else:
        print("num err!")
if __name__ == "__main__":
    num = input("please input a num:")
    fun(int(num))'''
        
'''输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数'''

def count(trs):
    sum1= 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    strs = trs.lower()
    for c in strs:
        if c >= 'a' and c <= 'z':
            sum1 += 1
        elif c >= '1' and c <= '9':
            sum2 += 1
        elif c == ' ':
            sum3 += 1
        else:
            sum4 += 1
    print "英文字母的个数是%d" % sum1
    print "数字的个数是%d" % sum2
    print "空格个数是%d" % sum3
    print "其他的个数是%d" % sum4
if __name__ == "__main__":
    #strs = input("please input a string:")
    count("sldfj ### ###")      
'''求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。'''
'''一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。'''
''' 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？'''
'''猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，
   见只剩下一个桃子了。求第一天共摘了多少。'''
'''题目：打印出如下图案（菱形）
 
 5    *
 6   ***
 7  *****
 8 *******
 9  *****
10   ***
11    *'''
'''for i in range(1,5):
     for j in range(3,0,-1):
         print(" ",end="")
     for k in range(1,2*i):
        print("*",end="")
     print("\n")
for m in range(3,0,-1):
    for n in range(1,4):
        print(" ",end="")
    for j in range(1,2*m):
        print("*",end="")
    print("\n")'''

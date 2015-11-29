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
'''输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数'''
'''求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。'''
'''def sums(num,n):
    sum1  = 0
    count = 0
    print("s=",end="")
    for i in range(0,n):
        sum1 += (10**i)*num
        if i < n-1:
            print("%d+" % sum1,end="")
        else:
            print("%d=" % sum1,end="")
        count += sum1
    print(count)
if __name__== "__main__":
     num = input("please input a number:")
     n = input("please input a number:")
     if int(num) >0 and int(num) < 9:
         sums(int(num),int(n))
     else:
         print("number error!!")'''
    
'''一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程找出1000以内的所有完数。'''
'''def ispefect(num):
    flag = True
    sums = 1
    temp = num
    for i in range(2,int(num/2)+1):
        while num%i == 0:
            sums += i
            num /= i
    if sums != temp:
        flag = False
    return flag
if __name__== "__main__":
     for i in range(1,1000):
         if ispefect(i):
             print(i)'''
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
'''
★
【程序22】
题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定
　　　比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出
　　　三队赛手的名单。 
'''
'''
【程序24】 
题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
'''
'''def sums(n):
    sum1 = 0.0
    sumed = 0.0
    a = 1
    b = 2
    for i in range(n):
        sum1 = float(b)/float(a)
        sumed += sum1
        if i == n-1:
            print ("%d/%d=" % (b,a)),
        else:
            print ("%d/%d+" % (b,a)),
        temp = a
        a = b
        b = temp + b
    print(sumed)
if __name__== "__main__":
    n = int(input("please input a number:"))
    sums(n)'''
'''
【程序25】 
题目：求1+2!+3!+...+20!的和
'''
'''def sums(n):
    sumed = 0
    temp = 1
    if n <= 0:
        print "error"
        return
    for i in range(1,n+1):
        for j in range(1,i+1):
            temp *= j
        if i == n:
            print "%d!=" % i,
        else:
            print "%d!+" % i,
        sumed += temp
        temp = 1
    print sumed
if __name__ == "__main__":
    n = int(input("please input a number:"))
    sums(n)'''
'''
【程序26】 
题目：利用递归方法求5!。
'''
def fun(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return -1
    else:
        return n * fun(n-1)
if __name__ == "__main__":
    n = int(input("please input a number:"))
    print fun(n)
'''
【程序27】 
题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''


# 注意sort list.sort()


# 关于多维度排序
dic=[{'name':'me','age':10},{'name':'you','age':20},{'name':'love','age':10}]
dic.sort(key=lambda x:(x['age'],len(x['name'])))
print(dic)




# 关于注释
    # 单行
print( '''iudhqwdhiuhq
   qdwhuqifoqi
   feoiqhfoq''')


# \续航符
print('dqwgdiugw\
wqdguyqdgiuqw\
dwqduiqud')
print("dguiawhduiqgw\nauywgduwgdyq\nqwgduiqgdqw")





# 数据类型
print(type(8/2))

# 注意结果是小数
print(9/3,9.0//3.0)

# 转义\
print("\"不知道填什么\"")
print(r"\"这是一个r\"")

#数据的相加减
r=1831293
print("给你一串数字：",r)
#print("再给你一串数字："+r)，这个不行

# 变量的传递
r=9
print(f"圆的r={r}")
print("圆的r={:>1d}".format(r))
print("圆的r=%10.2f"%r)# %10d %10.2f %s

a=int(input("a=")) # 注意 input赋值完是string
b=int(input("b="))
c=a*b
print(f"{a}*{b}={c}")
print("a*b=%d"%(a*b))
print(f"a*b={a*b}")
stock_code="0021873901"# 0不能作为数字的开头，所以用字符串
ths=0.1
print("%f"%ths) # 要输出0.1要注意精度

r=9
print(f"s={r**2}")# {}里面可以是表达式



# 关于布尔类型
# 非0，在if和while中皆可以被当作True 比如 if 1：   if not 0:



# 判断符号
b=3>5
print(b,type(b))


# if语句判断
if 8>=3 or 9<=2:
    print("呃不知道写什么%5.3f"%r)


# 值得注意的是python运行逻辑
def c():
    print(1)
    return 6
if c():
    print(c())
# 会print出 1 1 6







# 主包要写一个很牛的if嵌套语句
age=int(input("年龄："))
vip_level=int(input("vip等级："))
if age<=18:
   print("直接go")
else:
  if vip_level>=3:
     print("你也直接go")
  else :
     print("v我50")



   


# 主包要严肃写一个关于elif的代码了
age=19
date=8
level=9
if age>=18:
   print('LOVE ME')
elif date==8:
   print('\'LOVE ME\'')
elif level>=8:
   print('"LOVE\t ME"')
# 可以严肃的看出，elif开始执行的要求是楼上的返还False

# 一个可以减少输入的方法
if int(input('tell me your age:'))<=18:\
    print("ok well go directly")
elif int(input("tell me your level"))>=3:
    print("ok good go")
else :
    print("v me 50")

# 主包要写一个很牛的if嵌套语句
age=int(input("年龄："))
vip_level=int(input("vip等级："))
if age<=18:
   print("直接go")
else:
  if vip_level>=3:
     print("你也直接go")
  else :
     print("v我50")



   


# 主包要严肃写一个关于elif的代码了
age=19
date=8
level=9
if age>=18:
   print('LOVE ME')
elif date==8:
   print('\'LOVE ME\'')
elif level>=8:
   print('"LOVE\t ME"')
# 可以严肃的看出，elif开始执行的要求是楼上的返还False


# 关于while
t=0
c=0
while t<100:
   t+=1
   c+=1
print(c)

num=0
i=1
while i<=100:
   num+=i
   i+=1
print(num,i)



# 1st.注意randint（a，b）要写全，且是双闭区间
# 2nd. 注意while和int（input）的位置关系，不然会死循环，判断一次用if
import random
a=random.randint(1,10)
t=0

while int(input("guess a number"))!=a:
   t+=1

t+=1
print(a,t)



# 主包要写一个进阶版的了
import random
a=random.randint(1,10)
buer=True
t=0
while buer:
   b=int(input('guess a number'))

   if b==a:
      print("yes it is")
      buer=False
      t+=1

   elif b<a:
      print('small')
      t+=1
   else:
      print("big")
      t+=1
print(b,t)


# 主包要写一个循环嵌套循环的了
success=True
while success:
   print("please accept these ten roses as a gift")
   answer=input("do you accept my heartfelt love?")
   if answer=="yes":
      print("oh my love (家产nb)")
      success=False
   else:
      print("sorry,i have bothered you")


# 主包要写第二个嵌套了 while嵌套while了（楼上那个不算）
#num=1
#while num<=100:
   #j=1
   #while j <=10:
      #print(f"today i send her{j} rose,but i need to countine{10-j}")
      #j+=1
   #num+=1
#print("i get it")

# 关于print不换行
print("hello",end='')
print("world")
# 也就是说这个end=''要写在不换行的第一串字符串后面



# 主包要写一个99乘法表了嗯
i=1
while i<=9:
   j=1
   while j<i:
      print(f"{j}*{i}={i*j}\t",end="")
      j+=1
   if j==i:
      print(f"{j}*{i}={j*i}\t")
   i+=1


# 关于\t 其实是对齐（？每8个空格对齐一下
print("hello \tnice to \tmeet you")
print("sorry i\tam busy \tshall we meet on a latter time?")



# 主包还要写一个for的乘法表了
for i in range(1,10):
   for j in range(1,i+1):
      print(f"{j}*{i}={j*i}\t",end="")
   print()
# 或者改成<=i 然后在与第二个while平齐的地方写一个print（）


# for 语句 理论上不可以无限循环
# 主包要写一个很厉害的for循环语句
for item in "marvelous":
   print(f"{item}\t",end="")


n=0
for i in "duihwudhiuwqdhoiqwshi  qhdqoiwhdqoihdwhbxmxanliuwdoiquhoipouijkqlwhdiqowdpoqokqwhdoihqwdiohasjhqoqopwuopqjdq":
   if i=="a":
      n+=1
print(n)

   

lst=[1,56,8,32,23,6,89,23,7,9,3,4,5,8,6,1,2,3,7,9,0,6,4,2,2,2,2,2,2,2,1,1]
import copy
lst2=copy.copy(lst)
for i in lst2:
   if i==2:
      lst.remove(i)
print(lst)
for i in lst[:]:
   if i==1:
      lst.remove(1)
print(lst)

# 相较于while的条件判断循环（for依靠内部判断if也可以达成），for循环可以更好的控制次数
for i in "dwquiedy2o1yeo821y7891iqdhuiwqdyiwuqhg13uiwgddddddddddddeu":
   print('i love you')




# 如果把for语句的变量在外面print，会print出来变量最后被赋予的值,但最好把item在外面定义一下，这样显得主包优雅且高级嗯
item=0
for item in "what are you doing here?my friends?":
   pass
print(item)     



# 主包要写一个while嵌套for的雷霆语句了    注意while要元素不断改变，保证不会无线循环下去，for则不用考虑
i=1
while i <=10:
   for item in range(10):
      print(i,item)
   i+=1 



# 关于continue
i=0
while i <=10:
   if i!=5:
      print(i)
   else:
      i+=1   # 在continue下 也要保证循环条件变化，否则为死循环
      continue
   i+=1
   



# 关于break
i=0
while i <=10:
   if i !=5:
      print(i)
      i+=1
   else:
      break

# 个人觉得 continue和break可以应用于面对未知内容的元素集里面 跳过某个元素

# break and continue的应用和while for 交错
sum=10000
t=0
import random
for i in range(20):
  if sum>0:
   score=random.randint(1,10)
   if score<=5:
      t+=1
      continue # 这个continue完全不用写
   else:
      sum-=1000
      t+=1
  else:
   break
print(sum,t)

sum=10000
n=1
while sum>0:
   if n <=20:
      score=random.randint(1,10)
      if score<=5:
         n+=1
         continue  # 这个continue也不要写
      else:
         sum-=1000
         n+=1
   else:
      break
print(n,sum)


# 尝试写一个defination替代len（）,注意def里面也可以写print
def func(a):
   a=str(a)
   t=0
   for item in a:
      t+=1
   print(t)
func("i love you")


# def 的有趣小知识，如函数变量可以没有任何作用，单纯挂名，namely，无论传进来的参数如何，都不改变结果
his_answer=input("please respond to my love")
def g(a):
   print("beloved of her")
g(his_answer)


# 或者 可以不用传进来任何参数
def f():
   print("remedy my love")
f()

# 关于list（）有趣点，如下，将input的转化为list，是按输入的（包括空格）都转化为list，如input（1，2，3，4，5）lst1[1]=，再如input（12，3，4）lst1[1]=2
lst1=list(input())
print(lst1[1])


# 关于函数内部的print和print（函数）  如果print(func)，print出来的是函数里面return 如果没有return则是None且最底下代码运行顺序是从里到外
def check(tempature):
   tempature=float(tempature)
   if tempature>=37.5:
      print("you get a fever\t",end="")
   else:
      print("you are health")
   return "check is over"
print(check(input()))


# def 返回None等同于False  
def t():
   return None
b=0
b=t()
while not b:     # while 和if要执行，后面条件一定要是True
   print("no")
   break
if not b:
   print("yes")

def age(b):
   if int(b)>18:
      return "success"
if not age(7):
   print("no")





# 注意这个 return是sum所被赋予的值，而不是变量sum，所以最底下print（sum）会报错 故sum是一个局部变量
def lk():
   sum=0
   return sum
lk()
#print(sum)


# 函数内部全局变量改变要写 global 变量。不然直接对num改变会报错，但可以简单写成a=num-1（调用全局但不改变）
num=100
def ab():
    global num
    num+=1

ab()
print(num)


# 主包写了一个很nb的函数套函数
sum=50000
def withdraw():
   global sum
   change_sum=int(input("you want to do"))
   sum-=change_sum
   return sum

def add():
   global sum
   change_sum=int(input("you want to do"))
   sum+=change_sum
   return sum

def apply():
   a=int(input('''research click[1]
                  withdraw click[2]
                  deposit  click[3]
                  back     click[4]'''))
   if a==1:
      print(f"{sum}")
   elif a==2:
      withdraw()
      print(f"{sum}")
   elif a==3:
      add()
      print(f"{sum}")
   else:
      print("the service ends")
apply()




# 关于class 类似于定义了random.randint的random
class application:
   def g(self):
      print("love")
   def h(self):
      print("hate")
   def t(self):
      print("beloved")
application.g()
application.h()
application.t()
   




# 元组单元素要加,        (1)是int ("abx")是string  但无元素tuple写成（）就行了
a=(1)
print(a,type(a))
a=(1,)
print(a,type(a),len(a))


# 元组嵌套中
a=(1,(1,))
print(a)
# tuple.count
# tuple.index
# len(tuple)
# 但是tuple不可以修改，所以remove等不可使用



# 关于string
a_string='be involved with sb.'
s0=a_string[0]
print(s0)
s2=a_string.index('b')
print(s2)




# 注意！！！！！！！如果将list tuple set dictionary强行用str()转化，最后会变成"[1,2,3]" "{key=value:}" "{1,2,3,4}" "(1,2,3,4)"





# a_string[0]="do not b" 会报错，故本质上string与tuple一样不可以修改
print(a_string)
# 关于string中大字符串和小字符串,对于词组如number会定位第一个字符，namely，n
b="about  number  a"
print(b.index('number'))

# replace
nm='infinite'
nnm=nm.replace('i','t') # 本质上是creatue一个newstring 本身nm不被修改
print(nnm)
# replace可以用来删除 比如 string_1=string_1.replace("xxxx",'')





# 切片可以用来'删除掉'特定位置，比如string_1[:-2]为去掉末尾两个字符

# split
# split()不等同于split(' ') 且 split('')会报错
str_1='''       do you think the universe is infinite                      '''
lst1=str_1.split("  ")  # str.split("split the string as you like"),返回一个list,且split的字符不包含在内，如果字符在串1st则list中为''
print(lst1)



# 关于如何print出来
string_1='i love you so much'
lst1=string_1.split()
for i in lst1:
    print(i,end="")

# 或者合并成一个string
lst1=['love','you']
t=''  # 不可以写成None
for i in lst1:
    t=t+i

# strip
str_2=str_1.strip()      # strip()默认去除首尾空格 
print(str_2)
print(str_1)

str_3='athe i am the leader ehta' # strip从两端逐字符检查，若与strip()中相同则删去，遇到第一个不在()的字符，停止strip
str_4=str_3.strip('the')
print(str_4)
str_5='ththththththt'
print(str_5.strip('th'))

# 关于闰年的计算
import time
date=time.localtime()
year,month,day=date[:3]
month_day=[[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]]
flag=1 if year%400==0 or(year%4==0 and year%100!=0) else 0
print(sum(month_day[flag][:month-1])+day)



month_day=[31,28,31,30,31,30,31,31,30,31,30,31]
month_day[1]=29 if year%400==0 or (year%4==0 and year%100!=0) else 28
print(sum(month_day[:month-1])+day)


# 关于浮点数
# 浮点数有误差,可以用decimal解决，注意，转换的时候要用字符串
# 同时也可以进行误差修正 abs(a-b)<1e-6
from decimal import Decimal
print((0.1+0.2),Decimal('0.1')+Decimal('0.2'))




# 质数
lst1=[a for a in range(2,100) if 0 not in[a%d for d in range(2,a)]]
print(lst1)
t=0
for i in lst1:
    for j in lst1 :
        if j<=i:
            continue
        if i+j in lst1:
            t+=1
print(t)
lst1=[[a,b] for a in lst1 for b in lst1 if a+b in lst1]
print(len(lst1))





# 关于set,可以修改但不可以重复
set_1={"python",'python',"python",'''python'''} 
print(set_1)
set_1.add("love")
print(set_1)
set_2={"love",'me'}
# set 可以相减,但set_2中没有的元素不会出现在最后的结果里面
print(set_1-set_2,set_1) 
set_3=sorted(set_1,key=lambda x:len(x))  
print(set_3)
# set本身可以看作是无序的，可以用sorted（set，key=len）方式按照长度排序
# 自己输入的set和print后去重的set顺序也不一样
set_10086={'love','me','love','me','mother','father','please','love','me'}
print(set_10086)
# pop可以用来随机取出元素，应用在不放回的模型里面
# 依然可以用remove，因为pop索引下标，而remove索引第1次出现的具体元素
print(set_10086.pop())
# 关于取set的差集，注意是返还一个new_set
set_1={'love','me'}
set_2={'you','me'}
set_3=set_1.difference(set_2) 


# 以set_1为主体，.difference_update(set_2):
if not set_1.difference_update(set_2):
    print("love")
# 关于合并两个集合
set_3=set_1.union(set_2)
print(set_3)


# 关于挨个取set中的元素
set_1={1,2,3,4,5,6,7,8,9,0,10}
t=0
while t<11:                   # 此时set_1={},所以最好复制一个set_1
    print(set_1.pop())
    t+=1

set_1={1,2,3,4,5,6,7,8,9,0,10}
for item in set_1:
    print(item)



# set本身是无序的，所以不支持index和[:]

# set 的复制
set_1={1,2,3,4}
set_2=set_1.copy()
set_3=set(set_1)
print(set_1,'-'*30,set_2,"-"*30,set_2,"-"*30)


lst1=['i','love','zhengtai','oh','no']
set_1=set() # 定义空set不能用={}这个算作directionary 而应该是set_1=set()
t=0
while t<5:
    element=lst1[t]
    set_1.add(element)
    t+=1
print(set_1)
# 简洁版直接转换的
lst1=['love','me','love','you','love','her']
print(set(lst1))


# 关于字典，key不可以重复，如果定义了一个key对应了多个value，则取最后一个value
dictionary_1=dict()
dictionary_1={"love":'me',"love":"you","i":"love you"}
print(dictionary_1)
# 关于索引value
print(dictionary_1['love'])
# 关于字典嵌套字典，key不可以为字典
dictionary_1={"A":{"数学":'99',"语文":'99','英语':'100'},"B":{"语文":"98","数学":"88"}}
print(dictionary_1["A"]['数学'])

# 关于新增key
dictionary_1={1:'my love',2:'her love',3:'his love'}
dictionary_1[4]="our love"
# 关于修改value
dictionary_1[1]='you do not need my love'
print(dictionary_1)
# 关于删除key
print(dictionary_1.pop(2),dictionary_1)
# 关于清空
dictionary_2=dictionary_1
dictionary_2.clear()
print(dictionary_1)# 注意 list dictionary set 等可以被修改的，是动态的，=赋值本质是多一个命名
# 关于get全部key
dictionary_3={'a':'b','c':'b'}
a=dictionary_3.keys() # 取出来的keys不是列表，是键值,是迭代器，但也可以for  x in keys了
print(a,type(a))
# 遍历字典
for key in a:
    print(dictionary_3[key])
for key in dictionary_3:
    print(dictionary_3[key])



# (){}[]都是可以跨行的
# dict转tuple list set 都会丢失value 但string不会
dictionary_1={'a':1,'b':2}
print(set(dictionary_1),list(dictionary_1),tuple(dictionary_1 ))


# sorted(容器，reverse=True or False)  返还值都会变成list！！！！




# return多个值，用逗号隔开就行，不需要其他的
def g():
    a=1
    b="vigorous"
    return a,b
a,b=g()
print(b,a)

# 关键字传参,可以和默认传参混用，但必须默认在前
def g(a,b,c):
    print(f'{a}+{b}={c}')
g(a=1,c=2,b=3)

# 缺省参数(默认函数值)，设置默认值必须在最后
def h(a,b,c='love'):
    print(a,b,c)
h(1,2)
h(1,2,'not')
 # 可以被覆盖掉
# 不定长参数，可以传入不定数量个参数，返回值args是tuple
def g(*args):
    print(type(args),args)
g('a',1,2,3,4,3,4,5,2,4,5)
print(tuple(input()))

# 不定长关键字传参，返回值kwargs是字典
def m(**kwargs):
    print(type(kwargs),kwargs)
m(key='a',name=2) # m(**kwmargs)中传入的key，必须是不带""的字符串。

# 函数作为参数传递,函数可以确定数字传入运算逻辑，也可以确定运算逻辑然后传入数字
def fun(remember):
    result=remember(1,2,3,4)
    return result
def remember(a,b,c,d):
    return a**b+c**a+d
print(fun(remember))
# 上面可以运用于同一组数据不同运算

# lambda匿名函数,只能用一次，是临时变量，类似于迭代器
def gun(f):
    return f(1,2,3)
print(gun(lambda x,y,z:x+y+z**x+y**z))

# 注意第三个参数不是encoding，是省除默认参数，所以要写名字
# 注意1.txt test.txt.txt
f=open('1.txt','r',encoding='UTF-8')
print(f.read(3),'\t',f.read())
# f.read()返还一个string 
# read    所有read方式都是这样，比如下面的readlines)可以理解为迭代器，从上一次read结尾开始第二次read
f=open('1.txt','r',encoding='UTF-8')
print(f.readlines()) 
# readlines读每一行，包括空位符，然后形成列表

#readline,一次读取一行，与read相似
f=open('1.txt','r',encoding='UTF-8')
print(f.readline())

# 只有在终端，\t \n 才会被显示化




# for语句,每次读取一行
f=open('1.txt','r',encoding='UTF-8')
for i in f:
    print(i)

# 要及时关闭file，否则file面临无法修改
f.close()

# with open 自动关闭file
with open('1.txt','r',encoding='UTF-8')as f:
    print(f.readlines())



# 计数的几种方法   
# 值得注意的是 在readlines和readline中会print出来的\t \d 会被split掉

# read式
f=open('1.txt','r',encoding='UTF-8')
file_1=f.read()
print(file_1)
t=0
lst_1=file_1.split()
print(lst_1.count('by'))
t=0

# for遍历f split()会把\t \d 去掉
# review split（）里面什么也不写才会把' ''   ' '\n'去掉        如果是split（'a'）则不会去掉，且返回的list不包括a，且'\t ' '\n'保持\t \n 输出
with open ('1.txt','r',encoding='UTF-8')as f:
    for i in f:
        lst1=i.split()
        t+=lst1.count('by')
print(t)

# readlines
t=0
with open ('1.txt','r',encoding='UTF-8') as f:
    lst1=f.readlines()
    for i in lst1:
        lst2=i.split()
        print(lst2)
        t+=lst2.count('by')
print(t)
# w f有文件则clear后从头写，无文件则为创造一个文件。若文件名包括D:/则保存到相应位置，没有则保存到编码程序相应的文件夹内
with open('1.txt','w',encoding='UTF-8')as f:
   f.write('love')
# 三种存储的方式
f.flush()
f.close()
# 和with open的自动关闭
# a 有文件则追加，无则创建
with open('1.txt','a',encoding='UTF-8')as f:
   f.write()

# 综合
with open('1.txt','r',encoding='UTF-8')as f:
    for line in f:
        if line.count('测试')==0:              # if取出来的行末尾自带\n
            with open ('2.txt','a',encoding='UTF-8')as file_2:
                file_2.write(line)


# 捕获异常
try:
    f=open('4.txt','r',encoding='UTF-8')
    print(f.read())
    
except NameError as a:
    print('NameError')
except FileNotFoundError as a:
    print("FileNotFoundError")
# 捕获多个异常
try:
    print(1/0)
# 多个异常用tuple表示 as e,用e承接具体的异常，print(e)
except (FileExistsError,NameError,ZeroDivisionError)as e:
    print(e)




# 捕获全部异常
try:
    lst1=list(range(10))
    print(reversed(lst1))

except Exception as e:
    print(e)

# else与try大概共进退，finally是一定要执行的
try:
    print('love me')
except:
    print('\'love me\'')
else:
    print('love you indeed')
finally:
    print("devise rebellion")

# 如果有异常就不执行
try:
   print(1/0)
except:
   pass


# 异常的传递性
def func(sum):
    return sum(1,0)
def sum(a,b):
    return a/b
def fun():
   try:
    func(sum)
    print('love me')
   except:
       print('love you')
fun()





import time
print('thorn')
time.sleep(1)
print('clown')

# 两种import全部的方法，第二种更方便
import random
print(random.randint(1,10))
from random import *       
print(randint(1,10))
# import * 相当于import全部


# 别名，necklace
from math import sqrt as a
print(a(2**2+4**2))

import math as a
print(a.sqrt(8))





# from x import * 这个*取决于__all__=[]中有的函数，如果没有定义__all__=[]则默认全部
__all__=['a']
def a():
    print('vigorous')
def b():
    print('imitate')


# 关于 if __name__=='__main__':
# 是为了防止调用这个文件是顺手把文件内试运行的print一起调用出来





# json是不同语言之间的传递中枢，可以用来转化符合形式的string  or list套dictionary or dictionary
# json只能转化{} or [{},{}]
# 转化结果是string
from json import *
dictionary_1={'name':'12岁','age':'miracle'}
json_1=dumps(dictionary_1,ensure_ascii=False)       # 要保证中文被正确的转移出来，要ensure_ascii=False
print(type(json_1),json_1)


# 反向
string_1='[{"name":1,"age":3},{"pit":12,"miracle":4}]'  # 注意json转python的时候，key必须是""。
a=loads(string_1)
print(type(loads(string_1)))
print(type(a[0]))
print(a[0]['name'])




# pyechart
from pyecharts.charts import *
from pyecharts.options import *
line=Line()
line.add_xaxis(['chinese','the states','australia','italy'])
line.add_yaxis('len',[1,2,3,4])
# line.add_yaxis(label_opts=LabelOpts(is_show=False)) 可以用这个方式将具体数据隐掉





# 设置全局配置项
line.set_global_opts(
    title_opts=TitleOpts(title='gdp',pos_left='1%',pos_bottom='center'
    ),
    legend_opts=LegendOpts(is_show =True),
    toolbox_opts=ToolboxOpts(is_show=True),           # 这个为工具箱，如下载保存等
    visualmap_opts=VisualMapOpts(is_show=True)



)
line.render()



from pyecharts.charts import *
from pyecharts.options import *
map=Map()
data=[
    ('上海市',100),         # 这个名称要准确，写出'省 or 市'
    ('江苏省',400)
]
map.add('中国',data,'china')
map.set_global_opts(visualmap_opts=VisualMapOpts(is_show=True,is_piecewise=True,   # is_piecewise意思是自动校准
                                                              pieces=[{'min':1,'max':200,'label':'1-200','color':'#FF6666'}]
                                                )
                    )
map.render("love.html")




from pyecharts.charts import *
from pyecharts.options import *
map=Map()
data=[('扬州市',2),('南京市',2),('无锡市',2)]
map.add('江苏省',data,'江苏')     
# 默认是chinese，但如果是省份则直接写省份名



from pyecharts.charts import *
from pyecharts.options import *
bar_1=Bar()
bar_1.add_xaxis(['a','b','c'])
bar_1.add_yaxis('gdp',[1,2,3],label_opts=LabelOpts(position="right"))
bar_1.reversal_axis()
# bar.reversal_axis()用于反转x y轴,注意语法
bar_1.set_global_opts(title_opts=TitleOpts(title='gdp dynamic diagram',pos_left='center',pos_bottom='center'))
bar_1.render()

bar_2=Bar()
bar_2.add_xaxis(['a','b','c']) 
# .add_xaxis()里面是列表
bar_2.add_yaxis('gdp',[2,3,1],label_opts=LabelOpts(position='right'))
bar_2.reversal_axis()
bar_2.set_global_opts(title_opts=TitleOpts(title='gdp dynamic diagram',pos_left='center',pos_bottom='center'))
timeline=Timeline()
timeline.add(bar_1,'2029')
# timeline中的要表明好分隔的凭据，  注意，点位顺序取决于add的顺序！！！我先add2029，那2029就在2021的前面
timeline.add(bar_2,'2021')
timeline.add_schema(is_auto_play=True,is_loop_play=False,play_interval=2000)
# timeline.add_schema可以用来设置自动播放否？循环播放否？以及几个bar之间跳转的时间间隔
timeline.render()


# 注意，改变颜色：
from pyecharts.globals import *
timeline=Timeline({"theme":ThemeType.LIGHT})
# 在创建line的时候就定好theme

# 用异常捕捉代替if
dictionary_1={1:[1,2,3],2:[2,3,4],4:[1,9,2]}
for i in range(10):
    try:
        dictionary_1[i].append(0)
    except:
        dictionary_1[i]=[0]
print(dictionary_1)







# quiz，注意x y都要是列表   

dictionary={2020:[['美国',30],['中国',20]],
            2021:[['美国',20],['中国',40]]}       
from pyecharts.charts import *
from pyecharts.options import *

timeline=Timeline()
for key in dictionary:
    bar=Bar()
    lst1=[]
    lst2=[]
    for i in range(len(dictionary[key])):
        lst1.append(dictionary[key][i][0])
        lst2.append(dictionary[key][i][1])
    bar.add_xaxis(lst1)
    bar.add_yaxis('gdp',lst2)
    bar.reversal_axis()
    timeline.add(bar,key)
timeline.render()
    
# 防止dictionary中key是乱序版
from pyecharts.charts import *
from pyecharts.options import *

timeline=Timeline()
keys=sorted(dictionary.keys(),key=lambda x:x)
for key in keys:
    bar=Bar()
    lst1=[]
    lst2=[]
    for i in range(len(dictionary[key])):
        lst1.append(dictionary[key][i][0])
        lst2.append(dictionary[key][i][1])
    bar.add_xaxis(lst1)
    bar.add_yaxis('gdp',lst2)
    bar.reversal_axis()
    timeline.add(bar,str(key)) 
# ?很奇怪的一点是，名字这我传入int 也不报错，但最好传入string
    print(type(key))
timeline.render()
    
  


class student:
# 定义成员变量
    name=1
    age=2
    print(name,age)
# class里面的print不需要调用class就直接print

class love:
    number=2
    size=3
# 定义成员方法
# 注意要写self
    def love(self):
        print(f"{self.number}")
        
love_1=love()
love_1.love()
love_1.number=3
love_1.love()


# 自动传参
# 通过__init__(self,a,b,c)
class contempt:
    def __init__(self,name,age,heights):
        self.name=name
        self.age=age
        self.heights=heights
scorn=contempt(1,2,3)
print(scorn.name)


class contempt:
    name=None
# 这个异常捕捉是捕捉input非,两个整数，or非两个string
    age=None
    def g(self):
      try:
        return self.age+self.name
      except:
          print('please input interget')
    def __init__(self,name,age):
        self.name=name
        self.age=age
# 其实def要运行都要传入self
# 要传入参数就写成g(self,a,b)
      
    def h(self):   
        print('hatred')


# 以一个class的形式收录信息
class information:
    def __init__(self,name,age,birthplace):
        self.name=name
        self.age=age
        self.birthplace=birthplace
    def prin(self):
        print(f'name is{self.name},age is {self.age},birthplace is {self.birthplace}')
for i in range(3):
    stu_i=information(input('your name'),input('your age'),input('your birthplace'))
    print(f"this is {i+1} ")
    stu_i.prin()




class thorn:
    print(1)
    def g():
        print(2)
    try:
     def __init__():
        print(3)
    except:
        print('defect,defeat')
thorny=thorn()
# 注意这个异常捕捉。因为class在运行的时候是会运行一遍，(所以class里面的print会被直接执行)，
# 但第一遍运行的时候def__init__():本身没有错，所以不报错。
# 但第二遍thorn（）会直接调用__init__(),并且没有传入self，所以会报错，所以try应该写在thorny=thorn()上面(主包感觉这个try没有意义其实)



class gloomy:
    def __str__(self):
         return 'love'

# 注意这个__str__,return必须是一个string不可以是整数！！！
# __str__会让print 类对象变成print return
upset=gloomy()
try:
       print(gloomy)

# 直接print gloomy或者无__str__的upset 都会返回存储地址一样的东西（？
except:
     print("gloomy is wrong")
try:
     
     print(upset)
except:
     print("upset is wrong")



# __lt__
class contempt:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __str__(self):
        return f'{self.a}'
    def __lt__(self,other):
        return self.a<other.a
# 这个return随意定，大于可以返还True or False
# lt指的是小于 gt指的是大于，eq是等于，le ge

class semester:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __lt__(self,other):
       return self.a<other.a
# 注意 lt le mt me 按理说可以通过if判断其它大小关系！
# 但要考虑到规范，不能那样写
# 不对，是写<会调用lt
# 如果比较的方向在类里面没有定义会报错
# 但比较双方是同一类的话，除非只有eq，一般不会报错

semicircle=semester(1,2)
circle=semester(1,2)
print(semicircle!=circle)



class f:
    fly=2
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def g(self):
        print(self.a,self.b)
    __love='love'
# y=以__开头的变量是私有变量。和私有函数
# 私有变量在外部不可以被print，但可以被等效赋值，也就是创造了一个函数
# 私有函数在外部不可以被调用
    def __na(self):
        return 1
F=f(1,2)
F.g()
try:
    print(F.__love)



except:
    print("__ais unchangable")



# 注意，如果class里面的成员方法调用了成员变量，但在class外，对成员变量又进行的赋值等变化操作
# 方法里面的变量任然是原本的class里面定义好的那个(虽然同名，但内存里面不同名)
class stu:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __lt__(self,other):
        return self.a>other.b
    __age=9
    def f(self):
        print(self.__age)
       
    

stu1=stu(1,2)
stu1.__age=3
print(stu1.__age)
stu1.f()


# 这个私有变量也可以通过初始定义传参
class phone:
    def __init__(self,state):
        self.__state=state
# 没错，就是先定义一个变量，然后用__的变量接受
iphone=phone(False)
print(iphone.__state)



# class的一个小应用
class phone:
    def __init__(self,state):
        self.__state=state
    def __check_(self):
        if self.__state:
            print("5g")
            return True
        else:
            print('4g')
            return False
    def call(self):
        print(self.__check_())
        print('the system is running')
# 调用class里面的变量也好，函数也罢，都要加self！！不然就是调用全局函数了
          



        


iphone=phone(False)
iphone.call()




class judjement:
    sum=1000
    
    def __init__(self):
        if self.sum<=0:
            print('expense is run out')
    def apply(self):
        self.sum-=1000
      
      
j=judjement()   
j.apply()
print(j.sum)
j2=judjement()
print(j2.sum)



class jud:
    def __init__(self):
        self.balance=1000
# 建议所有可变的变量都这样定义
# 因为 如果class底下直接定义非数字，的可变变量如list，dictionary。
# 则都会变
class trial:
    lst1=[1,2]
t1=trial()
t2=trial()
t1.lst1.append(2)
print(t2.lst1)
class error:
    number=10
e1=error()
e2=error()
e1.number=1100
print(e2.number)


# 注意，父类的__init__(self)不会自动执行，要给父类赋值，要在子类中写
class stu:
    def __init__(self,a):
        self.a=a
    

        if self.a:
            print(2)
        else:
            print(3)
class stu_2:
    def __init__(self,b):
        self.b=b
        print(self.b)
class student(stu,stu_2):
    def __init__(self,a,b,c):
        stu.a=a
        stu_2.b=b
        self.c=c
        print(self.c)
c=student(10,20,30)
print(c.b,c.a)

# 如果stu(stu_1,stu_2,....,stu_n)中有重名的成员变量和方法，取最左边的那个
#
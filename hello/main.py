#! /usr/bin/env python
#coding=utf-8

# 多行缩进（减少缩进）：tab／shift+tab
# 上下移动： Alt + 方向键'↓'
# 删除行：Ctrl+d
# 自动完成：Alt+/ 
# 注释：Ctrl+／
# 窗口最大小：Ctrl+m
# 上一个编辑的位置：Ctrl+Q 
# 跳到某行：Ctrl+L

import sys

print ("hello")
print ("world")
print  (2**8)
jack = "okay"
print (jack)
for x in "spam":
    print (x)
print ("done")
print (sys.platform)

# from imp import reload   #要避免使用此用法
# reload (hello)

import myfile
print (myfile.title) #先导入模块，并获取模块属性

from myfile import title  #类似于从myfile模块中复制了title属性，使其成为接收者的直接变量
print (title)

exec(open("myfile.py").read()) #使用exec运行模块文件 ,类似于import 效果，但不会导入模块
exec(open("myfile.py")) #自动读取文件的内容


# L = [1,2]
# L.append(L)
# print (L)

print ("-" * 50)
# 第4章
# 程序--模块--语句--表达式--建立并处理对象
# 数字    1234
# 字符串  "spam"
# 列表   [1,2]
# 字典   ｛"quality"：4,"color":"red"}
# 元组  (1,'spam',4,'u')
# 集合  set('abc'),{'a','b','c'}
# 文件  myfile = open('eggs','r')
# 其它类型   类型，None ,布尔型
# 函数  def
# 模块  import
# 类  class

# 数字
print("数字===")
length = len(str(2**10))#求长度
print (length)
import math #数学模块
print (math.pi,math.sqrt(85))
import random #随机数模块
print (random.random())
print (random.choice([1,2,3,4])) #随机选择器

# 字符串：
print ("字符串====")
# s = "spam"
# print len(s),s[2],s[-1] #反向索引，从右边开始
# print s[1:3] #分片操作，从1开始直到3结束，共两个数据
# print s[1:],s[0:3],s[:-1],s[:] #左边默为0，右边默认是分片序列的长度
# print s+"xyz"  # + 号进行字符串合并
# print s*8 # *号字符串重复
# # 核心类型中，数字，字符串，元组是不可变的
# # 字典，列表可以自由改变
# print s.find("pa") #查找子字符串，若找到返回偏移量，若没有找到返回-1
# print s.replace("pa",'xyz')
# line = "aaa,bbb,ccc,ddd\n"
# print line.split(",")#以逗号 分开
# print line.upper() #转换为大写
# print line.isalpha()#测试字符串内容，数字，字母或其他
# print line.rstrip()#支掉字符串后面的空格字符
# help(line.strip)

# 列表：
print ("列表===")
# 一个任意类型的对象的位置相关的有序集合，类似于数组，但无固定类型的约束
l = [123,"spam",1.23]
l.append("ni") #扩充列表大小，并在列表尾部插入一项
print (l)
print (l.pop(2)) #移除给定偏移量的一项，让列表减小
print (l)

l.sort()#排序
l.reverse()#反转
# col2 = [row[1] for row in M] # 把矩阵M的每个row中的row[1],放在一个新的列表中，组成一个新的列表

# 字典 键：值对,映射关系
print("字典===")
d = {"food":"spam","quality":4,"color":"red"}
print d["food"]
d["quality"] +=1 #
print d

d={}
d["name"] = "bob"
d["job"] = "it"
d["age"] = 30
print d
print d["name"]

# 引入for
d = {"a":1,"b":2,"c":3}
print d
ks = list(d.keys())
print ks
ks.sort()
print ks
for key in ks:
    print (key,"=>",d[key])
for c in "spam":
    print c.upper()

    
x = 4
while x>0:
    print ("spam!" *x)
    x -=1

squares = [x ** 2 for x in [1,2,3,4,5]] #迭代方法
print squares   
# 等同于下面的for
squares =[]
for x in [1,2,3,4,5]:
    squares.append(x ** 2)
print squares


# if not "f" in d:
    # print ("missing")

# 元组：
print ("元组========")
t = (1,2,3,4)
print t
t + (5,6)
print t,t[0]
print t.index(3)#求数据对应的index
print t.count(4)#求数据出现的次数


# 文件：
f = open("data.txt","w")
f.write("hello")
f.write(",world")
f.close()
f = open("data.txt","r")#读操作 r 默认可以忽略
text = f.read()
print text,text.split()#分隔符对字符串进行切片
text2 = open("data.txt","rb").read()
print text2[4:8]


# 集合
print ("集合=====")
x = set("spam")
print x

if type(l) == type([]):
    print "yes"


# 用户定义的类
print ("定义类====")
class Worker:
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self,percent):
        self.pay *= (1.0 +percent)
bob = Worker("bob smith",50000)
sue = Worker("sue jones",60000)
print bob.lastName()
sue.giveRaise(.10)
print sue.pay

# 不可变性：数字，字符串，元组
# 序列：字符串，列表，元组，可对位置进行排序

# 数字类型
# 八进制： 0o1,0o2
# 16进制： 0x01,0x02
# 2进制： 0b1,0b1001

# oct函数将十进制数转换为八进制数
# hex函数会将十进制数转换为十六进制数
# bin函数会将十进制数转换为二进制数

x = set("abcde")
y = set("bdxyz")
print x
print x-y
print x|y
print x&y
print x^y
x.add("f")
print x
x.update("x")
print x
x.remove("b")
print x
for item in x:
    print (item *3)

print ("-" * 50)
# 第6章：动态类型
# a = 3  表示变量a变成对象3的一个引用，在内部，变量事实上是到对象内存空间的一个指针
# python中变量名没有类型，对象才有类型
# a = 3
# a = "string"
# a = 1.23 
# 上面只是把a修改为对不同的对象的的引用
# python中，每当一个变量名被赋予一个新的对象，之前的那个对象占用的空间就会被回收（如果它没有被其他的变量名或对象所引用的话），这种自动回收对象空间的技术叫垃圾收集

# 共享引用：多个变量名引用了同一个对象
# a = 3
# b = a

L1 = [2,3,4]
L2 = L1[:]  # copy L1对象,从头到尾的分片
L1[0] = 24
print L1,L2

import copy  #通用的复制任意对象类型的调用
L2 = copy.copy(L1)
L3 = copy.deepcopy(L1) #copy嵌套对象结构（如嵌套了列表的一个字典）
print L2,L3

# 检查是否相等
# ==操作符，测试两个被引用的对象是否有相同的值
# is操作符，检查对象的同一性，如果两个变量名精确地指向同一个对象，则返回true
# == : 操作符测试值的相等性
# is:表达式测试对象的一致性，测试是否是同一个对象（也就是说在同一个内存地址中）

print ("-" * 50)
# 第7章：字符串
s = b'spam'
# s = u'spam' #使用的unicode字符串
# s1 + s2 #合并，重复
# s * 3
# s[i] #索引，分片，求长度
# s[i:j]
# len(s) #返回多少个字节
# s.find("a") #搜索
# s.rstrip() #移除空格
# s.replace("pa","xx")#替换
# s.split(",") #分隔
# s.isdigit()#内容测试
# s.endswith("spam")#结束测试 
print s

# myfile = open(r"c:\new\text.dat","w") #r表示关闭转义机制
# myfile = open("c:\\new\\text.dat","w")

# 偏移和分片：位置偏移从左至右（偏移0为第一个元素），而负偏移是由末端右侧开始计算（偏移-1为最后一个元素）
# s[0]
# s[-2] #取倒数第二个元素
# s[i:j]
# s[1:3]#取偏移为1的元素，直到但不包括偏移为3的元素
# s[1:]#取偏移为1的元素，直到末尾
# s[:3]#取偏移为0的元素，直到但不包括偏移为3之间的元素
# s[:-1]#取偏移为0的元素，直到但不包括最后一个元素之间的元素
# s[:]#取偏移为0到末尾的元素
# s[1:10:2] #取偏移值1-9之间，间隔一个元素的元素
print (sys.argv)
print int("42") #int将字符串转换为数字
print str(42) #将数字转换为字符串
s = "42"
i = 1
print int(s)+1
print ord("s")

# 字符串是不可变序列
# 若要改变
s = "splot"
s = s.replace("pl","pamal")
print s


s = "spammy"
l =  list(s) #以任意序列中的元素创立一个新的列表
print l
l[3] = "x"
print l

s = "".join(l) #join 将列表合成一个字符串
print s

line = "aaa bbb ccc"
cols = line.split()#将一个字符串侵害为一个子字符串的列表
print cols

line2 = "aaa,bbb,ccc"
cols2 = line2.split(",")
print cols2

list = list("spam")
print ("first = {0[0]},third = {0[2]}".format(list))
print ("the %s side %s %s" % ("bright","of","life"))

# 不可变性：数字，字符串，元组，不可变集合
# 可变性：列表，字典，可变集合

# 第8章： 列表与字典

# 列表：
# 任意对象的有序集合
# 通过偏移读取
l = []
l = ["a",["b","c"]]
# l = list("spam")
# l = list(range(-4,4))

# l1 + l2  #合并，重复
# l * 3
# for x in l: print (x) #迭代，成员关系 
# 3 in l
# l.append(4)  #末尾增加
# l.extend([5,6,7])
# l.insert(0,8)#插入
# l.count(6)#次数
# l.sort()#排序
# l.reverse()#反转
# del l[6] #删除index对应的值
# del l[2:4] #删除指定index范围内元素
# l.pop()#删除最后一个元素
# l.pop(1)#删除指定index元素
# l.remove("a")#删除某个元素
l = [x ** 2 for x in range(5)]
# l = list(map(ord,"spam"))
print l


for x in [1,2,3]:
    print (x)

print ("后进先出LIFO  last-in-first-out")
l = []
l.append(1)
l.append(2)
print l
l.pop()
print l
##############################
print ("先进先出FIFO  first-in-first-out")
l = []
l.append(1)
l.append(2)
l.reverse()
print l
l.pop()
print l

# 字典
d = {}
d = {"spam":2,"eggs":3}
d = {"food":{"ham":1,"egg":2}}
print d
# d = dict(zip(keyslist,valsist))
# d = dict(name = "bob",age =2)
# d.keys()#键
# d.values()#值
# d.items()#键 + 值
# d.copy()#副本
# d.get(key,default)
# d.update(d2) #合并
# d.pop(key) #删除
# len(d)
# d[key] = 4 #新增/修改键
# del d[key]#根据键删除条目
# list(d.keys())#字典视图

d = {"spam":3,"eggs":5}
print d["eggs"]
d2 = {"toast":4,"muilk":5}
d.update(d2)
print d
####################################
table = {"python":"Guido van Rossum",
         "perl":"Larry Wall",
         "tcl":"John Ousterhout"}
language = "python"
creater = table[language]
print creater
for lang in table:
    print (lang,table[lang])

###################################
L = [0]*100
L[99] = "SPAM"
print L

L = {}
L[99] = "SPAM"
print L
###################################
rec = {}
rec["name"] ="xin"
rec["age"] = "33"
rec["job"] = ["it","worker"]
print rec, rec["name"],rec["job"][1]

# 创建字典
dict(name = "mel",age =45)
dict([("name","mel"),("age",45)])

d = dict.fromkeys(["a","b"],0) #对所有键初始化
print d
k = d.keys()
print k
v = d.values()
print v
l = d.items()
print l
for k in d.keys():
    print k
for key in d:
    print key

####################################    
# 第9章：元组，文件 
# 元组：由任意对象组 组成，不可变 ，圆括号，具有列表大多数属性
# 有序的对象集合
tmp = ("cc","aa","dd","bb")
print tmp
t = tuple(tmp)
print t

t = (1,2,3,4,5)
L = [x + 20 for x in t]
print L

t = (1,2,3,2,5)
print t.index(2)#求2 首次出现的index
print t.count(2)#求2 共出现几次

# 文件：
# open函数会创建一个python文件对象
# output = open(r"c:\soam","w")#创建输出文件
# input = open("data","r")#创建输入文件 
# input = open("data")
# aString  = input.read()#把整个文件读进单一字符串

# aString = input.read(N)#读取之后的N个字节到一个字符串
# aString = input.readline()#读取下一行到一个字符串
# aList = input.readlines()#读取整个文件到字符串列表
# output.write(aString)#写入字节到文件 
# output.write(aList)#把列表内所有字符串写入文件 
# output.close()#手动关闭(当文件 收集完成后关闭文件 )
# output.flush()#把输出缓冲区刷到硬盘中，但不关闭文件 
# anyFile.seek(N)#修改文件位置到偏移量N处以便进行下一个操作
# for line in open("data"): use line
# open("f.txt",encoding="latin-1")
# open("f.bin","rb")
# w:写文件
# r:读文件 
# a：文件尾部追加内容
# +：同时为输入输出打开文件

# 输出文件总是缓冲的，表示写入的文件可以不会立即自动从内存转换到硬盘，而关闭一个文件，或者运行其flush方法，迫使缓存的数据进入硬盘
myfile = open("data.txt","w")
myfile.write("hello txet file\n")
myfile.write("goodbye text file")
myfile.close()

myfile = open("data.txt")
str = myfile.readline()#读取一行到字符串
str2 = myfile.readlines()#读取整个文件到字符串列表
print myfile.read()#读取整个文件到一个字符串
print str
print str2

# 迭代一行一行读取文件内容
for line in open("data.txt"):
    print (line)

# pickle存储python的原生对象
# pickle模块能让我们直接在文件中存储几乎任何python对象，不需要把字符串换来换去
# 必须以二进制模式打开对象文件，因为pickle程序创建和使用一个bytes字符串对象
# 并且这些对象意味着二进制模式文件
d= {"a":1,"b":2}
f = open("datafile.pkl","wb")
import pickle
pickle.dump(d,f)
f.close()

print("="*50)
f =open("datafile.pkl")
e = pickle.load(f)
print e

L = [1,2,3]
D = {"a":1,"b":2}
A = L[:] #复制序列 （序列：字符串，列表，元组）
B = D.copy()#复制字典
print A,B


# 字典比较:手动比较排序的键/值列表，items字典方法和内置的sorted足够了
d1 = {"a":1,"b":2}
d2 = {"a":1,"b":3}
print d1 == d2,d1 <d2
print sorted(d1.items())
print sorted(d1.items()) < sorted(d2.items())

# 真假
# 数字如果非零，则为真
# 对象如果非空，则为真
# None,总被认为是假,表示一个空的占位，是一个真正的对象，且有一块内存，表示是某些内容，而不是没有内容
L = [None]*10 #分配一个10项的列表
print L

# BOOL类型
print bool("spam") #测试一个对象的布尔值

# 对象类型
# python中所有一切都是某种类型的对象，任何对象的类型都是类型为"type"的对象


print("="*50)
# 第10章：语句和语法
text = "my python"
# if elif else #选择
if "python" in text:
    print "text"

        
        # for else #迭代
# while else# 一般循环
# pass #空占位符
# while True:
    # pass
# break 退出循环
# continue 循环继续
# def 函数和方法
def f(a,b,c):
    print (a+b+c)
# return 函数结果
def fun(a,b,c):
    return a+b+c
# yield 生成器函数
def gen(n):
    for i in n:
        yield i*2
# from 属性访问
#from sys import stdin
# class 创建对象
class Subclass():
    staticData = []
    def method(self):
        pass
# assert 调试检查
#assert  x>y,"x too small"
# with/as 环境管理器
#with open("data.txt") as file:
#    fun(file)

# del 删除引用
del list
    
    
# while True:
    # reply = raw_input("enter text:")
    # if reply == "stop":
        # break
    # elif not reply.isdigit():#判断如果不是数字，输出bad
        # print ("bad!"*8)
    # else:
        # num = int(reply)
        # if num < 20:
            # print ("low")
        # else:            
            # print(num**2)            
# print ("bye")


# while True:
    # reply = raw_input("enter text:")
    # if reply == "stop":
        # break
    # try:
        # num = int(reply)
    # except:	
        # print ("bad!"*8)
    # else:
        # print(int(reply)**2)            
# print ("bye")
 

# python 3.0
# input()
# print ()
# python 2.6
# raw_input()
# print
    
# 多目标赋值语句
a =b =c ="sapm"

# 变量名没有类型，但对象有


# 第12章 if测试和语法
# if xx:
    # test
# elif xx1:
    # test1
# else:
    # test2

y = 4
x = y // 2
print x

print("="*50)
file = open("data.txt")
while True:
    line = file.read() #一次加载所有
    # line = file.readline()#按行读取
    #line = file.read(10)#按块读取
    if not line: break
    print line

for line in open("data.txt").readline():
    print (line)

# range是一个迭代器，根据需要产生元素
print range(5)
# [0, 1, 2, 3, 4]
print range(2,5)
# [2, 3, 4]
print range(0,10,2)
# [0, 2, 4, 6, 8]

for i in range(3):
    print(i,"python")
    
# zip也是一个迭代对象,将序列中的并排的元素重新配成对
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print zip(L1,L2)
# [(1, 5), (2, 6), (3, 7), (4, 8)]
for (x,y) in zip(L1,L2):
    print(x,y,"--",x+y)
# (1, 5, '--', 6)
# (2, 6, '--', 8)
# (3, 7, '--', 10)
# (4, 8, '--', 12)
        
# zip构造字典
keys = ["spam","eggs","toast"]
vals = [1,3,5]
print zip(keys,vals)
# [('spam', 1), ('eggs', 3), ('toast', 5)]

D2 = {}
for (k,v) in zip(keys,vals):
    D2[k] = v
print D2
# {'toast': 5, 'eggs': 3, 'spam': 1}

f = open("data.txt")
print next(f)
print next(f) #next(f)等同于 f.__next__(),读取下一行


L = [1,2,3]
I = iter(L)
while True:
    try:
        x = next(I)
    except StopIteration:
        break
    print x**2     

# 第15章 文档
# dir函数: 抓取对象内可用所有属性列表

dir(sys)

# 文档字符串
'''
    
'''
# module.class.method.__doc__

# help函数 获取文档帮助
help(sys.getrefcount)


# 第16章 函数
print("="*50)
print
print ("hello")

# def 函数名(参数)：
# 没有返回值的函数自动返回一个none对象
# def语句是实时执行的
# 函数定义
def times(x,y):
    return x*y
# 函数调用
print times(2,4)

# eg.
def intersect(seq1,seq2):
    res = []
    for x in seq1:
        if x in seq2:
            res.append(x)
    return res
s1 = "spam"
s2 = "scam"
print intersect(s1,s2)











































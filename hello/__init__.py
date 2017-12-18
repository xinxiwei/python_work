#! /usr/bin/env python
#coding=utf-8

import os
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
print length
import math #数学模块
print math.pi,math.sqrt(85)
import random #随机数模块
print random.random()
print random.choice([1,2,3,4]) #随机选择器

# 字符串：
print ("字符串====")
s = "spam"
print len(s),s[2],s[-1] #反向索引，从右边开始
print s[1:3] #分片操作，从1开始直到3结束，共两个数据
print s[1:],s[0:3],s[:-1],s[:] #左边默为0，右边默认是分片序列的长度
print s+"xyz"  # + 号进行字符串合并
print s*8 # *号字符串重复
# 核心类型中，数字，字符串，元组是不可变的
# 字典，列表可以自由改变
print s.find("pa") #查找子字符串，若找到返回偏移量，若没有找到返回-1
print s.replace("pa",'xyz')
line = "aaa,bbb,ccc,ddd\n"
print line.split(",")#以逗号 分开
print line.upper() #转换为大写
print line.isalpha()#测试字符串内容，数字，字母或其他
print line.rstrip()#支掉字符串后面的空格字符
# help(line.strip)

# 列表：
print ("列表===")
# 一个任意类型的对象的位置相关的有序集合，类似于数组，但无固定类型的约束
l = [123,"spam",1.23]
l.append("ni") #扩充列表大小，并在列表尾部插入一项
print l
print l.pop(2) #移除给定偏移量的一项，让列表减小
print l

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

print ("-" * 50)
# 第7章：字符串
# s = b'spam'
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



























































































































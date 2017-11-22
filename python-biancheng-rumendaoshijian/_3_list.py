#! /usr/bin/env python
#coding=utf-8

# 列表
bicycles = ['trek','cannoda','redline','specialized']
print (bicycles)

print (bicycles[0])
print (bicycles[0].title())
print (bicycles[-1].title())

#修改列表元素
print ("--"*30)
motocycles = ['honda','yamaha','suzuki']
print (motocycles)
motocycles[0] = 'toyota'
print (motocycles)

#列表添加元素
print ("--"*30)
motocycles.append("bmw")
print (motocycles)

#列表插入元素
print ("--"*30)
motocycles.insert(0,'www')
print (motocycles)

#删除元素
print ("--"*30)
del motocycles[0]
print (motocycles)

#pop删除末尾元素
print ("--"*30)
pop_motocycle = motocycles.pop()
print (motocycles)
print (pop_motocycle)

#删除元素
print ("--"*30)
motocycles.remove('suzuki')
print (motocycles)

#永久排序
print ("--"*30)
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print (cars)

#临时排序
print ("--"*30)
cars = ['bmw','audi','toyota','subaru']
print (cars)
print (sorted(cars))
print (cars)


#倒着打印列表
cars = ['bmw','audi','toyota','subaru']
print (cars)
cars.reverse()
print (cars)


#列表长度
cars = ['bmw','audi','toyota','subaru']
length = len(cars)
print (length)







#! /usr/bin/env python
#coding=utf-8

# �б�
bicycles = ['trek','cannoda','redline','specialized']
print (bicycles)

print (bicycles[0])
print (bicycles[0].title())
print (bicycles[-1].title())

#�޸��б�Ԫ��
print ("--"*30)
motocycles = ['honda','yamaha','suzuki']
print (motocycles)
motocycles[0] = 'toyota'
print (motocycles)

#�б����Ԫ��
print ("--"*30)
motocycles.append("bmw")
print (motocycles)

#�б����Ԫ��
print ("--"*30)
motocycles.insert(0,'www')
print (motocycles)

#ɾ��Ԫ��
print ("--"*30)
del motocycles[0]
print (motocycles)

#popɾ��ĩβԪ��
print ("--"*30)
pop_motocycle = motocycles.pop()
print (motocycles)
print (pop_motocycle)

#ɾ��Ԫ��
print ("--"*30)
motocycles.remove('suzuki')
print (motocycles)

#��������
print ("--"*30)
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print (cars)

#��ʱ����
print ("--"*30)
cars = ['bmw','audi','toyota','subaru']
print (cars)
print (sorted(cars))
print (cars)


#���Ŵ�ӡ�б�
cars = ['bmw','audi','toyota','subaru']
print (cars)
cars.reverse()
print (cars)


#�б���
cars = ['bmw','audi','toyota','subaru']
length = len(cars)
print (length)







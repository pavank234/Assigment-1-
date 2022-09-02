
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
print(ages)
minimumValue=min(ages)
maximumValue=max(ages)
ages.insert(0,minimumValue)
ages.append(maximumValue)
print(ages)
mid=len(ages) // 2
medianResult=(ages[mid] + ages[~mid])/2
print("Minimum age:",minimumValue)
print("Maximum age:",maximumValue)
print("Median of age:",round(medianResult,2))
print("Average of age:",round((sum(ages)/len(ages)),2))
print("Range of age:",maximumValue-minimumValue)


dog={}
dogItems=(('Name','Tommy'),('Color','White'),('Breed','Bulldog'),('leg',4),('Age',5))
dog.update(dogItems)
student={}
studentItem=(('First_name','James'),('Last_name','Smith'),('Gender','Male'),('Age',25),('Marital_status','Single'),('Skill',['Java','Python']),
             ('Country','USA'),('City','Kansas York'),('Address','8519 Overland Park'))
student.update(studentItem)
print("Lenght of the student dictionary:",len(student))
print('Value of skills:',student['Skill'],"data type:",type(student['Skill']))
student['Skill']=['Python','AI']
print('Dictionary keys:',student.keys())
print('Dictionary values:',student.values())


from itertools import combinations
  
b_s= ('Hari', 'Narms','Vineeth',"Taru")

sib=[]
for i in range(1,len(b_s)+1):
    temp = combinations(b_s, i)
    sib.extend(list(temp))
sib=tuple(sib)
print(sib)


it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print('Length of the set It_companies:',len(it_companies))
it_companies.add('Twitter')
company={'BLACK AND WEETCH','VAM','Infosys','Cognizant'}
it_companies.update(company)
it_companies.remove('Facebook')
'''
What is the difference between remove and discard?
The remove() method will raise an error if the specified item does not exist, and the discard() method will not
'''
print('Union of A and B',A.union(B))
print('Intersection of A and B',A & B)
print(A.issubset(B))
print(A.isdisjoint(B))
print('Join A with B',A.union(B))
print('Join B with A',B.union(A))
print('Symetric difference between A and B:',A.symmetric_difference(B))
A.clear()
B.clear()
it_companies.clear()
listIntoSet=set(age)
print(listIntoSet)
print(len(age)==len(listIntoSet))


import math as n
radius=30
_area_of_circle_= n.pi * (radius**2)
print('Area:',round(_area_of_circle_,2))
_circum_of_circle_=2*n.pi*radius
print('Circumstance:',round(_circum_of_circle_,2))
radius=int(input('Enter radius of circle:'))
print('Area:',round(n.pi*(radius**2),2))


str='I am a teacher and I love to inspire and teach people'
listIntoSet=set(str.split())
print('Number of unique words in given sentence:',len(listIntoSet))


print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')


radius= 10
area=3.14*radius**2
print('The area of a circle with radius {} is {} meters square.'.format(radius,area))



L1=[]
result=[]
N=int(input('Number of student:'))
for i in range(N):
    wt=int(input('Enter weight of the student:'))
    L1.append(wt)
    result.append(round(wt*0.453592,2))
print(L1)
print(result)

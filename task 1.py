#create a list
my_list=[1,2,3,4,5]
print('original list = ',my_list)
my_list.append(7)
my_list.remove(3)
my_list[0]=6
print('new list = ',my_list)
print()

#create a dictionary
my_dict={'name':'raj','age':12,'gender':'male'}
print('original dictionary',my_dict)
my_dict['city']='mumbai'
del my_dict['age']
my_dict['name'] = 'elijah'
print('new dictionary',my_dict)
print()

#create a set
my_set={1,2,3,4,5}
print('original set',my_set)
my_set.add(7)
my_set.remove(2)
my_set.discard(1)
print('new set',my_set)



Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_dict={'key1':'value1','key2':'value2'}
>>> my_dict
{'key1': 'value1', 'key2': 'value2'}
>>> my_dict=['key2']
>>> my_dict={'key1':'value1','key2':'value2'}
>>> my_dict['key1']
'value1'
>>> prices_lookup={'apple':0.8,'orange':1.2,'milk':1}
>>> prices_lookup['milk']
1
>>> #dictionaries can also have lists when defining the value use the [] to input your list
>>> #you can also have dictionaries in dictionaries {{}}
>>> #k2:{Dsd}
>>> d={'k1':['a','b','c']}
>>> mylist=d['k1']
>>> letter=mylist[2]
>>> letter
'c'
>>> letter.upper()
'C'
>>> #or
>>> d['key1'][2].upper()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    d['key1'][2].upper()
KeyError: 'key1'
>>> d['k1'][2].upper()
'C'
>>> #add to dictionary
>>> d
{'k1': ['a', 'b', 'c']}
>>> d['k2']=30.333
>>> d
{'k1': ['a', 'b', 'c'], 'k2': 30.333}
>>> #overwrite
>>> d['k1']='NEW VALUE'
>>> d
{'k1': 'NEW VALUE', 'k2': 30.333}
>>> d.keys()
dict_keys(['k1', 'k2'])
>>> d.values()
dict_values(['NEW VALUE', 30.333])
>>> d.items()
dict_items([('k1', 'NEW VALUE'), ('k2', 30.333)])
>>> 
=============================== RESTART: Shell ===============================
>>> t=(1,2,3)
>>> mylist=[1,2,3]
>>> type.t
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    type.t
AttributeError: type object 'type' has no attribute 't'
>>> type(t)
<class 'tuple'>
>>> type(mylist)
<class 'list'>
>>> len(t)
3
>>> t=('one',3)
>>> t
('one', 3)
>>> t[1]
3
>>> #similar to a list
>>> t=('a','a','b')
>>> t.count('a')
2
>>> t.index('a')
0
>>> mylist
[1, 2, 3]
>>> mylist[0]='wow'
>>> mylist
['wow', 2, 3]
>>> t[0]=1
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t[0]=1
TypeError: 'tuple' object does not support item assignment
>>> #meant to happen
>>> #tuples become a good solution when you are writing large programs and you want to make sure items aren't reassigned
>>> 
=============================== RESTART: Shell ===============================
>>> myset=set()
>>> myset
set()
>>> myset.add(1)
>>> myset
{1}
>>> #looks like a dictionary but it's not as it doesn't have key value pairs
>>> myset.add(2)
>>> myset
{1, 2}
>>> myset.add(2)
>>> myset
{1, 2}
>>> #have to add unique values so won't repeat it
>>> mylist[2,2,2,2,2,3,3,3,3,3,4,4,4,1,1,1]
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    mylist[2,2,2,2,2,3,3,3,3,3,4,4,4,1,1,1]
NameError: name 'mylist' is not defined
>>> mylist=[2,2,2,2,2,3,3,3,3,3,4,4,4,1,1,1]
>>> set(mylist)
{1, 2, 3, 4}
>>> set('Mississippi')
{'i', 'M', 'p', 's'}
>>> 
=============================== RESTART: Shell ===============================
>>> True
True
>>> type(False)
<class 'bool'>
>>> 1>2
False
>>> 1==1
True
>>> #== is checking for equality
>>> b=None
>>> b
>>> type(b)
<class 'NoneType'>
>>> 
=============================== RESTART: Shell ===============================
>>> %%writefile myfile.txt
SyntaxError: invalid syntax
>>> 

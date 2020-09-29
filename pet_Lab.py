#!/usr/bin/env python
# coding: utf-8

# In[6]:


class Pet:
    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.owner = 'no one'
        
    def set_owner(self, owner):
        self.owner = owner
        
    def __str__(self):
        return 'Hi I am %d yrs and my name is %s \nI am not house trained and %s owns me' % (self.number, self.name, self.owner)

    def train(self):
        self.number += 0
        
garfield = Pet('Garfield', 3)
x=1
print (f'{x}:{garfield}')
x+=1
print (f'{x}:{garfield}')
x+=1
print (f'{x}:{garfield.owner}')
garfield.set_owner('Jon')
x+=1
print (f'{x}:{garfield}')
garfield.train()
x+=1
print (f'{x}:{garfield}')

#create a list with about 4 pets

pets= [garfield, Pet('Beethoven',2), Pet('Jake',5), Pet('Stuart',7)]

for p in pets:

  x+=1

  print(f'\n{x}:{p}')


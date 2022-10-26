#!/usr/bin/env python
# coding: utf-8

# In[1]:


fin = open("/Users/jg198/Desktop/words.txt")


# In[2]:


fin.readline()


# In[3]:


line = fin.readline()
word = line.strip()
word


# In[4]:


fin = open("/Users/jg198/Desktop/words.txt")
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
word


# In[5]:


fin = open("/Users/jg198/Desktop/words.txt")
for word in fin:
    if len(word) > 20:
        print(word)
word


# In[6]:


fin = open("/Users/jg198/Desktop/words.txt")

def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True  

for line in fin:
    word = line.strip()
    if has_no_e(word):
        print (word)
word


# In[ ]:





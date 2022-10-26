#!/usr/bin/env python
# coding: utf-8

# In[1]:


t = [[1, 2], [3], [4, 5, 6]]
nested_sum(t)


# In[2]:


t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t):
    total = 0
    for j in range(len(t)):
        if type(t[j]) == list:
            total += nested_sum(t[j])
        else:
            total += t[j]
    return total
print(nested_sum([[1, 2], [3], [4, 5, 6]]))


# In[4]:


t = [1, 2, 3]
new_list=[]
total = 0
for j in range (0, len(t)):
    total+=t[j]
    new_list.append(total)
print(new_list)


# In[ ]:





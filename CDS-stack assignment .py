#!/usr/bin/env python
# coding: utf-8

# STACK

# In[3]:


# push operation 
stack = []
stack.append(1) # adding elements to the stack using append 
stack.append(2)
stack.append(3)
print("Stack items:", stack)  


# In[4]:


# Pop opearion
def pop(stack):
    if len(stack) == 0:
        return None
    else:
        return stack.pop()

stack = [1, 2, 3]
print("Initial Stack:", stack)
print("Popped Element:", pop(stack)) # removes the last element from the stack 


# In[ ]:





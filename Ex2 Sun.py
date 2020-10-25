#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pulp


# In[3]:


import pulp
A= pulp.LpVariable('A',lowBound = 0)
B= pulp.LpVariable('B',lowBound = 0)

profit=pulp.LpProblem('Maximum Profit',pulp.LpMaximize)
profit+=200000*A+80000*B,'Objective Function'
profit+=3000*A+900*B<=75000
profit+=-5*A+1*B<=0
profit+=A<=15
profit+=A>=5

profit.solve()

print('Decision Variable Values: ')

for variable in profit.variables():
    print(variable.name,'=',variable.varValue)
    
print('\nMaximum Profit:')
pulp.value(profit.objective)


# In[ ]:





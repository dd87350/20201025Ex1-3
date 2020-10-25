#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pulp


# In[6]:


import pulp
A= pulp.LpVariable('A',lowBound = 0)
B= pulp.LpVariable('B',lowBound = 0)

profit=pulp.LpProblem('Minimum Profit',pulp.LpMinimize)
profit+=0.10*A+0.15*B,'Objective Function'
profit+=5*A+10*B>=45
profit+=4*A+3*B>=24 
profit+=0.5*A>=1.5

profit.solve()

print('Decision Variable Values: ')

for variable in profit.variables():
    print(variable.name,'=',variable.varValue)
    
print('\nMinimum Profit:')
pulp.value(profit.objective)


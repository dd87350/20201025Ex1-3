#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pulp


# In[3]:


import pulp
T= pulp.LpVariable('T',lowBound = 0)
C= pulp.LpVariable('C',lowBound = 0)

profit=pulp.LpProblem('Maximum Profit',pulp.LpMaximize)
profit+=7*T+5*C,'Objective Function'
profit+=3*T+4*C<=2400
profit+=2*T+1*C<=1000 
profit+=C<=450
profit+=T>=100

profit.solve()

print('Decision Variable Values: ')

for variable in profit.variables():
    print(variable.name,'=',variable.varValue)
    
print('\nMaximum Profit:')
pulp.value(profit.objective)


# In[ ]:





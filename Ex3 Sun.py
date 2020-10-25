#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pulp


# In[21]:


import pulp
C3= pulp.LpVariable('C3',lowBound = 0)
C9= pulp.LpVariable('C9',lowBound = 0)
D= pulp.LpVariable('D',lowBound = 0)
E= pulp.LpVariable('E',lowBound = 0)

profit=pulp.LpProblem('Minimum Profit',pulp.LpMinimize)
profit+=0.12*C3+0.09*C9+0.11*D+0.04*E,'Objective Function'
profit+=E>=7.5
profit+=C3+C9>=22.5
profit+=C9+D<=15
profit+=C3+C9+D+E==50

profit.solve()

print('Decision Variable Values: ')

for variable in profit.variables():
    print(variable.name,'=',variable.varValue)
    
print('\nMinimum Profit:')
pulp.value(profit.objective)


# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# In[20]:


#How much does US Medical Insurance Cost?

import csv

insurance_costs_list = []

with open('insurance.csv', newline = '') as insurance_csv:
    insurance_reader = csv.DictReader(insurance_csv)
    for row in insurance_reader:
        insurance_costs_list.append(row['charges'])

def as_currency(amount):
    if amount >= 0:
        return '${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)
        
insurance_costs_list = [float(x) for x in insurance_costs_list]
user_count = len(insurance_costs_list)
total_insurance_costs = as_currency(sum(insurance_costs_list))
min_insurance_cost = as_currency(min(insurance_costs_list))
max_insurance_cost = as_currency(max(insurance_costs_list))

print(str(user_count) + " Americans spent a combined total of " + str(total_insurance_costs) + 
      " on medical insurance this year. The minimum amount spent by an individual was " 
      + str(min_insurance_cost) + " The maximum amount spent by an individual was "
     + str(max_insurance_cost) + ".")


# In[ ]:





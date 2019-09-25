#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
HW - 02 (Build a Webscraper)
Submitted by: Gaurav Nagal
'''


# In[106]:


from requests import get
import re
import pandas as pd
import time


# In[107]:


# defining empty lists
male_list = []
female_list = []


# In[108]:


for i in range(0, 50):
    time.sleep(1) # wait for 1 second
    resp = get("https://www.theyfightcrime.org/")
    
    # cite: https://docs.python.org/2/library/re.html
    # Male group
    male = re.search("(He's.*?She's)", resp.text)
    male_text = male.group(0).replace(". She's", "")
    male_list.append(male_text)
    
    # Female group
    female = re.search("(She's.*? They fight crime!)", resp.text)
    female_text = female.group(0).replace(". They fight crime!", "")
    female_list.append(female_text)
    
    d = {'Male': male_list, 'Female': female_list}
    df = pd.DataFrame(d)


# In[109]:


# Saving as csv
with open('Male_list.csv', 'w') as csvFile:
    csvFile.write("\n".join(male_list))
with open('Female_list.csv', 'w') as csvFile:
    csvFile.write("\n".join(female_list))


# In[ ]:





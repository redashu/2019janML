#!/usr/bin/env python
# coding: utf-8

# In[7]:


from  sklearn  import tree


# In[13]:


# this data is about apple and orange
#  smooth 1 red  100 and pred 80 
#  bumpyu 0   orange 150 and porange  130 
features=[[1,100],[1,80],[0,150],[0,130]]
label=["apple","apple","orange","orange"]


# In[14]:


#  calling  desicion tree classifier 
algo=tree.DecisionTreeClassifier()
# now time for training this algo 
trained_algo=algo.fit(features,label)


# In[25]:


#  time for giving input 
prediction=trained_algo.predict([[0,110]])
print(prediction)


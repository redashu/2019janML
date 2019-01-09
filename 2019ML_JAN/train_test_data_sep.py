#!/usr/bin/env python
# coding: utf-8

# In[12]:


from  sklearn.datasets  import  load_iris
from  sklearn.model_selection  import  train_test_split
from sklearn  import  tree


# In[3]:


iris=load_iris()


# In[4]:


#  now  splitting  training and testing dataset testing data 10% 
split_data=train_test_split(iris.data,iris.target,test_size=0.2)


# In[5]:


train_data,test_data,train_target,test_target=split_data


# In[10]:


features=train_data
label=train_target


# In[13]:


#  calling  clf
dsc_clf=tree.DecisionTreeClassifier()
trained=dsc_clf.fit(train_data,train_target)


# In[19]:


output=trained.predict(test_data)


# In[21]:


#  to check  accuracy  of algo 
from   sklearn.metrics  import accuracy_score
acc=accuracy_score(test_target,output)
print("algo accuracy score is ",acc)


# In[ ]:





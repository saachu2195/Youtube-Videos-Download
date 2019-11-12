#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pytube')


# In[4]:


from pytube import YouTube


# In[5]:


yt = YouTube("https://www.youtube.com/watch?v=8u5ZVWDOtSA")


# In[6]:


yt.streams.all()


# In[8]:


yt.streams.filter(progressive=False).all()


# In[12]:


audio = yt.streams.filter(only_audio=True).all()
audio


# In[14]:


yt.streams.get_by_itag(251).download()


# In[ ]:





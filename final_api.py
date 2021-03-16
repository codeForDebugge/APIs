#!/usr/bin/env python
# coding: utf-8

# In[14]:


from keras.preprocessing import image
import numpy as np
from keras.models import load_model
import os

folders=os.listdir('datasets/train/')
img_to_dict={}
images=[]
labels=[]
for i,f in enumerate(folders):
    img_to_dict[i]=f


def prediction(img):
        img=image.load_img(img,target_size=((224,224)))
        imgFinal=image.img_to_array(img)
        imag=np.array(imgFinal)
        imag=imag.reshape((-1,224,224,3))
        model=load_model("mod.h5")
        p=model.predict(imag)
        s = np.max(p)
        i = p = np.argmax(p)
        return s, img_to_dict[i]



# In[19]:





# In[ ]:





# In[ ]:





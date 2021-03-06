import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os,cv2
def image_loader_celeba(path,image_size):
    data = []
    img_path = os.path.join(path)
    img_list= os.listdir(img_path)
    print(len(img_list))
    for i in range(16):
        number = np.random.randint(0,len(img_list))
        data_img = cv2.imread(img_path + "/" + img_list[number])
        data_img = cv2.cvtColor(data_img,cv2.COLOR_BGR2RGB)
        data_img = np.array(data_img)
        data_img = cv2.resize(data_img,image_size,interpolation = cv2.INTER_CUBIC)
        data.append(data_img)
    
    data = np.array(data)
    print(data.shape)
    return data

def image_processing(dataset):
    data = tf.cast(dataset,tf.float32)
    data = (data - 127.5) / 127.5
    return data 

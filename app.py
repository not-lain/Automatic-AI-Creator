from tkinter import filedialog
from tkinter import *
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import class_weight
from keras.layers import Input, Conv2D, BatchNormalization, MaxPooling2D, Dropout, Flatten, Dense, GlobalAveragePooling2D
from keras.models import Sequential
from keras.applications.mobilenet_v2 import MobileNetV2
import tensorflow as tf

def train(parent):
    train_datagen = ImageDataGenerator(rescale=1./255,
                                       rotation_range=10,
                                       width_shift_range=0.05,
                                       height_shift_range=0.05,
                                       zoom_range=0.05,
                                       horizontal_flip=True,
                                       vertical_flip=True,
                                       brightness_range=[0.5, 1.4],
                                       validation_split=0.2)
    train_generator = train_datagen.flow_from_directory(directory=parent,
                                                        batch_size=5,
                                                        target_size=(224, 224),
                                                        shuffle=True,
                                                        class_mode="binary",
                                                        subset="training")

    validation_generator = train_datagen.flow_from_directory(directory=parent,
                                                            batch_size=5,
                                                            target_size=(
                                                                224, 224),
                                                            shuffle=False,
                                                            class_mode="binary",
                                                            subset="validation")
    base_model = MobileNetV2(input_shape=(224, 224, 3),
                             include_top=False,
                             weights='./mobilenet_v2_weights_tf_dim_ordering_tf_kernels_1.0_224_no_top.h5')


    base_model.trainable = False

    model = tf.keras.Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(1024, activation='relu'),
        Dropout(rate=0.2),
        Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer=tf.optimizers.Adam(learning_rate=0.00008),
                loss="binary_crossentropy",
                metrics=["accuracy"])
    history = model.fit(train_generator, epochs=10,
                        batch_size=5,
                        validation_data=validation_generator)
    
    model.save("model.h5")


window = Tk()
window.geometry("860x500")
window.title("Automatic-AI-Creator")

parent = ''


def input_function():
    global parent
    global var
    parent = filedialog.askdirectory()
    text.set(f"folder : {parent} ")
    


def extraction():
    global parent
    print(parent)
    train(parent)
    text2.set("model status = trained")
    text3.set("accuracy = \n{parse value from history} ")
    text4.set("model is saved successfully")





btn = Button(text="Input", command=input_function).pack()


text = StringVar()
text.set("click on input ! ")
label = Label(window, textvariable=text).pack()


btn2 = Button(window, text="Build", command=extraction).pack()

text2 = StringVar()
text2.set("model status = not trained yet")
text3 = StringVar()
text3.set("accuracy = 0")
text4 = StringVar()
text4.set("model not saved yet")
label2 = Label(window, textvariable=text2).pack()
label3 = Label(window, textvariable=text3).pack()
label4 = Label(window, textvariable=text4).pack()

btn2 = Button(window, text="Host The AI", command=extraction).pack()

window.mainloop()

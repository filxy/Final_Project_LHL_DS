# -*- coding: utf-8 -*-
"""dfd

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TV6B0vwpwSUc8nINhBNMBVVhDbxu8p_6
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile test-app.py
# import streamlit as st
# import cv2
# import numpy as np
# import tensorflow as tf
# from PIL import Image
# import matplotlib.pyplot as plt
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from DeepFake-Classifier import *
# 
# 
# 
# st.header("Deep Fake Detection")
#     
# menu_items={
#         'image or video prediction' ,
#         'Web-cam prediction',
#         'About'
# }
# 
# 
# 
# @st.cache
# def load_image(uploaded_files):
#   img = Image.open(uploaded_files)
#   return img
# 
# def save_uploadedfile(uploaded_files):
#   with open(os.path.join("tempDir",uploaded_files.name),"wb") as f:
#     f.write(uploaded_files.getbuffer())
#     return st.success("Saved File:{} to tempDir".format(uploaded_files.name))
# 
# def main():
#   #Menu = ["image or video prediction", "Web-cam prediction","About"]
#   choice = st.sidebar.selection("Menu",menu_items)
#   if choice == "image or video prediction":
#     st.subheader("Predict deep fake images or videos")
#     uploaded_files = st.file_uploader("upload an image or video",type=['png','jpeg','jpg','mp4','avi','mov'])
#     if uploaded_files is not None:
#       file_details = {"FileName":uploaded_files.name,"FileType":uploaded_files.type}
#       st.write(file_details)
#       st.write(type(uploaded_files))
#       img = load_image(uploaded_files)
#       st.image(img,height=256,width=256)
#       with open(uploaded_files.name,"wb") as f:
#         f.write(uploaded_files.getbuffer())
#         st.succes("file saved! Please click Generate Prediction")
#         Generate_pred = st.button("Generate Prediction")
#         
#     
#   elif choice == "Web-cam prediction":
#     st.subheader("Predict with web-cam")
#     img_file_buffer = st.camera_input("Take a picture")
#     if img_file_buffer is not None:
#       # To read image file buffer with OpenCV:
#       bytes_data = img_file_buffer.getvalue()
#       cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
#       # Check the type of cv2_img:
#       # Should output: <class 'numpy.ndarray'>
#       st.write(type(cv2_img))
#       Generate_pred = st.button("Generate Prediction")
#       if Generate_pred:
#         meso = Meso4()
#         meso.load("saved_model/Meso4_DF")
# if(type == 'jpg'or'png'or'jpeg'):
#   #image generator to predict images over webcam
#   dataGenerator = ImageDataGenerator(rescale=1./255)
#   generator = dataGenerator.flow_from_directory(
#         'tempDir',
#         target_size=(256, 256),
#         batch_size= 1,
#         class_mode='binary',
#         subset='training')
# 
# X, y = generator.next()
# print('Predicted :', meso.predict(X), '\nReal class :', y)
# 
# # Rendering image X with label y for MesoNet
# X, y = generator.next()
# 
# # Evaluating prediction
# print(f"Predicted likelihood: {meso.predict(X)[0][0]:.4f}")
# print(f"Actual label: {int(y[0])}")
# print(f"\nCorrect prediction: {round(meso.predict(X)[0][0])==y[0]}")
# 
# # Showing image
# plt.imshow(np.squeeze(X));
# st.write("predictions closer to 0 are fake and predictions closer to 1 are real")
# 
# if(type == 'mp4'or'avi'or'mov'):
#   #loading weights for video detection
#   Classifier = Meso4()
#   Classifier.load("Meso4_F2F.h5")
#   #video prediction
#   predictions = compute_accuracy(Classifier, "tempDir")
#   for video_name in predictions:
#     #print('`{}` video class prediction :'.format, predictions[video_name])
#     print('`{}` video class prediction :'.format(video_name), predictions[video_name][0])
# 
# st.write("predictions closer to 0 are fake and predictions closer to 1 are real")
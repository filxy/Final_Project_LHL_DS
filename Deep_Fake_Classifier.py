{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"name":"Deep_Fake_Classifier","provenance":[],"collapsed_sections":[],"machine_shape":"hm","authorship_tag":"ABX9TyN/JlSTq8UoVjs95qJ+ggWo"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"},"accelerator":"GPU"},"cells":[{"cell_type":"code","execution_count":null,"metadata":{"colab":{"base_uri":"https://localhost:8080/"},"id":"lVAVfTwDxL-X","executionInfo":{"status":"ok","timestamp":1645254733656,"user_tz":300,"elapsed":798,"user":{"displayName":"Rj Filxy","photoUrl":"https://lh3.googleusercontent.com/a-/AOh14GgJp4N_ugdO21IlRgr4JNhwDF5oYZfme92ZO50_yfs=s64","userId":"06153042309472469951"}},"outputId":"ac2af1d6-d079-4b8a-d107-679c70777835"},"outputs":[{"output_type":"stream","name":"stdout","text":["Drive already mounted at /content/drive/; to attempt to forcibly remount, call drive.mount(\"/content/drive/\", force_remount=True).\n"]}],"source":["# Mounted google drive\n","from google.colab import drive\n","drive.mount('/content/drive/')"]},{"cell_type":"code","source":["#!pip install face-recognition"],"metadata":{"id":"KDNky01dxpG3"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["#!pip install face_recognition\n","#!pip install imageio-ffmpeg\n","#!pip install imageio==2.16.0\n","#!pip install pillow\n","#!pip install ffmpeg-python\n","#!pip install tensorflow==2.5.0rc1"],"metadata":{"id":"dcVtr4HU0quF"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["# Imported libraries\n","from IPython.display import display, Javascript, Image\n","from google.colab.output import eval_js\n","from base64 import b64decode, b64encode\n","import numpy as np\n","import cv2\n","import PIL\n","import io\n","import html\n","import time\n","import matplotlib.pyplot as plt\n","from tensorflow.keras.layers import Input, Dense, Flatten, Conv2D, MaxPooling2D, BatchNormalization, Dropout, Reshape, Concatenate, LeakyReLU\n","from tensorflow.keras.preprocessing.image import ImageDataGenerator\n","from tensorflow.keras.optimizers import Adam\n","from tensorflow.keras.models import Model\n","import random\n","from os import listdir\n","from os.path import isfile, join\n","\n","from math import floor\n","from scipy.ndimage.interpolation import zoom, rotate\n","\n","import imageio\n","import face_recognition"],"metadata":{"id":"l-3m60rjxpOE"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["# Creating a Dictionary to define Image Dimensions\n","image_dimensions = {'height':256, 'width':256, 'channels':3}"],"metadata":{"id":"C6lnMTvVxaYJ"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["# Create a Classifier class\n","\n","class Classifier:\n","    def __init__():\n","        self.model = 0\n","    \n","    def predict(self, x):\n","        return self.model.predict(x)\n","    \n","    def fit(self, x, y):\n","        return self.model.train_on_batch(x, y)\n","    \n","    def get_accuracy(self, x, y):\n","        return self.model.test_on_batch(x, y)\n","    \n","    def load(self, path):\n","        self.model.load_weights(path)"],"metadata":{"id":"4rnRG58zxbFs"},"execution_count":null,"outputs":[]},{"cell_type":"code","source":["# Create a MesoNet class using the Classifier\n","\n","class Meso4(Classifier):\n","  # Created init method\n","    def __init__(self, learning_rate = 0.001):\n","        self.model = self.init_model()\n","        # Defined a gradient Descent optimizer variable and set the LR in the constructor\n","        optimizer = Adam(lr = learning_rate)\n","        # Defined parameters to compile the model\n","        self.model.compile(optimizer = optimizer,\n","                           loss = 'mean_squared_error',\n","                           metrics = ['accuracy'])\n","    # Create method called init_model\n","    def init_model(self): \n","      #Create a variable X and assigned input layer to pass the image dimensions\n","        x = Input(shape = (image_dimensions['height'],\n","                           image_dimensions['width'],\n","                           image_dimensions['channels']))\n","        # Convoulutional Layers\n","        x1 = Conv2D(8, (3, 3), padding='same', activation = 'relu')(x)\n","        # Batch Normalization\n","        x1 = BatchNormalization()(x1)\n","        # Max Pooling \n","        x1 = MaxPooling2D(pool_size=(2, 2), padding='same')(x1)\n","\n","        x2 = Conv2D(8, (5, 5), padding='same', activation = 'relu')(x1)\n","        x2 = BatchNormalization()(x2)\n","        x2 = MaxPooling2D(pool_size=(2, 2), padding='same')(x2)\n","        \n","        x3 = Conv2D(16, (5, 5), padding='same', activation = 'relu')(x2)\n","        x3 = BatchNormalization()(x3)\n","        x3 = MaxPooling2D(pool_size=(2, 2), padding='same')(x3)\n","        \n","        x4 = Conv2D(16, (5, 5), padding='same', activation = 'relu')(x3)\n","        x4 = BatchNormalization()(x4)\n","        x4 = MaxPooling2D(pool_size=(4, 4), padding='same')(x4)\n","        \n","        y = Flatten()(x4)\n","        y = Dropout(0.5)(y)\n","        y = Dense(16)(y)\n","        y = LeakyReLU(alpha=0.1)(y)\n","        y = Dropout(0.5)(y)\n","        y = Dense(1, activation = 'sigmoid')(y)\n","\n","        return Model(inputs = x, outputs = y)"],"metadata":{"id":"rLPgScOyxd7q"},"execution_count":null,"outputs":[]}]}
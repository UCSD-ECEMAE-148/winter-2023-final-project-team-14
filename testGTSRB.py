import pandas as pd
import cv2
import os
import tensorflow.keras as keras
import numpy as np
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential
import tensorflow as tf

data_dir = './GTSRB/Training'

def preprocess(img):
    return cv2.resize(img, (64, 64), interpolation = cv2.INTER_AREA)

list_images = []
output = []

for dir in os.listdir(data_dir):
    i = 0
    if dir == '.DS_Store' :
        continue
    inner_dir = os.path.join(data_dir, dir)
    csv_file = pd.read_csv(os.path.join(inner_dir,"GT-" + dir + '.csv'), sep=';')
    for row in csv_file.iterrows():
        if i < 100:
            img_path = os.path.join(inner_dir, row[1].Filename)
            img = cv2.imread(img_path)
            img = img[row[1]['Roi.X1']:row[1]['Roi.X2'],row[1]['Roi.Y1']:row[1]['Roi.Y2'],:]
            img = preprocess(img)
            list_images.append(img)
            output.append(row[1].ClassId)
        i += 1

input_array = np.stack(list_images)
train_y = keras.utils.to_categorical(output)

randomize = np.arange(len(input_array))
np.random.shuffle(randomize)

x = input_array[randomize]
y = train_y[randomize]

split_size = int(x.shape[0]*0.6)
train_x, val_x = x[:split_size], x[split_size:]
train1_y, val_y = y[:split_size], y[split_size:]

split_size = int(val_x.shape[0]*0.5)
val_x, test_x = val_x[:split_size], val_x[split_size:]
val_y, test_y = val_y[:split_size], val_y[split_size:]

epochs = 10
batch_size = 16

input_shape = Input(shape=(32, 32,3))

model = Sequential([
    Conv2D(16, (3, 3), activation='relu', input_shape=(64,64,3), padding='same'),
    BatchNormalization(),
    Conv2D(16, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.2),
    
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    Conv2D(32, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.2),
    
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    Conv2D(64, (3, 3), activation='relu', padding='same'),
    MaxPooling2D(pool_size=(2, 2)),
    Dropout(0.2),
    
    Flatten(),
    Dense(units=2048, activation='relu'),
    Dropout(0.2),
    Dense(units=1024, activation='relu'),
    Dropout(0.2),
    Dense(units=128, activation='relu'),
    Dropout(0.2),
    Dense(units=43, input_dim=2048, activation='softmax'),
])

model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=1e-4), metrics=['accuracy'])
trained_model_conv = model.fit(train_x.reshape(-1,64,64,3), train1_y, epochs=epochs, batch_size=batch_size, validation_data=(val_x, val_y))

model.evaluate(test_x, test_y)
model.save('./model/keras_model.h5')

model = keras.models.load_model("./model/keras_model.h5")
tf.saved_model.save(model, "./model/tmp_model")
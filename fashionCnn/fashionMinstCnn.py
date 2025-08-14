import tensorflow as tenf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import fashion_mnist
import numpy as npfunc
import matplotlib.pyplot as plotGraph

# This loads the data , i leverage on keras website. https://keras.io/api/datasets/fashion_mnist/
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

#restructure for CNN
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

#Will now create a list for image section, gotten from keras  website. https://keras.io/api/datasets/fashion_mnist/

itemNames = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))


test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc:.4f}")

#This predicts two images
predictions = model.predict(x_test[:2])
for i, pred in enumerate(predictions):
    print(f"Image {i+1} predicted as: {itemNames[npfunc.argmax(pred)]}")
    plotGraph.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plotGraph.title(f"Prediction: {itemNames[npfunc.argmax(pred)]}")
    plotGraph.savefig(f"predictions/prediction_image{i+1}.png")
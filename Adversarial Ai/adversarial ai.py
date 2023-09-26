# Had Help from Chat GPT with making this work

import tensorflow as tf
import numpy as np

# Load a pre-trained MobileNetV2 model
model = tf.keras.applications.MobileNetV2(include_top=True, weights='imagenet')

# Load and preprocess the cat image
image_path = 'cat.jpg'
image = tf.keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
image = tf.keras.preprocessing.image.img_to_array(image)
image = tf.keras.applications.mobilenet_v2.preprocess_input(image)

# Get the initial prediction
initial_prediction = model.predict(np.expand_dims(image, axis=0))
initial_class = tf.argmax(initial_prediction, axis=1)
initial_class_label = tf.keras.applications.mobilenet_v2.decode_predictions(initial_prediction)[0][0][1]
print(f'Initial prediction class: {initial_class.numpy()[0]} {initial_class_label}')


target_class = 713  # The class index for "photocopier" in ImageNet

# Define a loss function to maximize the target class probability
@tf.function
def loss(image):
    prediction = model(image)
    target_probability = prediction[0, target_class]
    return -target_probability

# Generate the adversarial image
image_batch = tf.Variable(np.expand_dims(image, axis=0), trainable=True)  # Add batch dimension

# Create an optimizer
optimizer = tf.keras.optimizers.Adam(learning_rate=0.01)

epochs = 100
for epoch in range(epochs):
    with tf.GradientTape() as tape:
        loss_value = loss(image_batch)

    grads = tape.gradient(loss_value, image_batch)
    optimizer.apply_gradients([(grads, image_batch)])

    if epoch % 10 == 0:
        print(f'Epoch {epoch}, Loss: {loss_value.numpy()}')

# Get the final prediction
final_prediction = model.predict(image_batch)
final_class = tf.argmax(final_prediction, axis=1)
final_class_label = tf.keras.applications.mobilenet_v2.decode_predictions(final_prediction)[0][0][1]
print(f'Final prediction class: {final_class.numpy()[0]} {final_class_label}')

# Save the adversarial image
adversarial_image = tf.keras.preprocessing.image.array_to_img(image_batch.numpy()[0])
adversarial_image.save('adversarial_cat.jpg')


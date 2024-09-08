import tensorflow as tf
import pickle
mnist=tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test)=mnist.load_data()
x_train,x_test=x_train/255.0,x_test/255.0
model=tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128,activation='relu'))
model.add(tf.keras.layers.Dense(10,activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam' , metrics=[ 'sparse_categorical_accuracy'])
model.fit(x_train,y_train,batch_size=32,epochs=5)
model.evaluate(x_test,y_test,batch_size=32,verbose=2)
with open('my_model.pkl', 'wb') as f:
    pickle.dump(model, f)
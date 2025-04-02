""" Built-in function to define 4 different neural network architectures to find best fitted model """

import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

def build_models():
    
    tf.random.set_seed(1234)
    model_1 = Sequential(
        [
            tf.keras.Input(shape = (11,)),
            Dense(5, activation = 'relu'),
            Dense(8, activation = 'relu'),
            Dense(6, activation = 'relu'),
            Dense(1, activation = 'sigmoid')
        ],
        name = 'model_1'
    )

    model_2 = Sequential(
        [
            tf.keras.Input(shape = (11,)),
            Dense(9, activation = 'relu'),
            Dense(3, activation = 'relu'),
            Dense(7, activation = 'relu'),
            Dense(5, activation = 'relu'),
            Dense(1, activation = 'sigmoid')
        ],
        name = 'model_2'
    )

    model_3 = Sequential(
        [
            tf.keras.Input(shape = (11,)),
            Dense(2, activation = 'relu'),
            Dense(4, activation ='relu'),
            Dense(8, activation = 'relu'),
            Dense(1, activation = 'sigmoid')
        ],
        name = 'model_3'
    )

    model_4 = Sequential(
        [
            tf.keras.Input(shape = (11,)),
            Dense(6, activation = 'relu'),
            Dense(3, activation = 'relu'),
            Dense(6, activation = 'relu'),
            Dense(2, activation = 'relu'),
            Dense(7, activation = 'relu'),
            Dense(4, activation = 'relu'),
            Dense(1, activation = 'sigmoid')
        ],
        name = 'model_4'
    )

    models_list = [model_1, model_2, model_3, model_4]

    return models_list
        

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Activation, ReLU, LeakyReLU, Add, Flatten, Dense
from tensorflow.keras.layers import Conv2D, DepthwiseConv2D, SeparableConv2D
from tensorflow.keras.layers import MaxPooling2D, UpSampling2D, ZeroPadding2D, GlobalAveragePooling2D, AveragePooling2D
from tensorflow.keras.layers import Dropout, SpatialDropout2D
from tensorflow.keras.layers import BatchNormalization

from tensorflow.keras.layers import Concatenate, Softmax, GlobalMaxPooling2D
from tensorflow.keras.layers import PReLU, Reshape


def _TestModel(input_shape):
    x = Input(shape=input_shape, name='data_src_0')
    inputs = x

    outputs = []

    _x = ReLU(name="data_dst_0")(x)
    outputs.append(_x)

    model = Model(inputs=inputs, outputs=outputs)
    return model


def TestModel(input_shape, drop=0.2):
    x = Input(shape=input_shape, name='data_src_0')
    inputs = x

    x = SeparableConv2D(16, (3, 3), strides=(1, 1), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = SeparableConv2D(8, (3, 3), strides=(1, 1), padding="same", activation="relu")(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = SeparableConv2D(8, (3, 3), strides=(1, 1), padding="same", activation="relu")(x)
    x = UpSampling2D(size=(2, 2))(x)
    x = SeparableConv2D(16, (3, 3), strides=(1, 1), padding="same", activation="relu")(x)
    x = UpSampling2D(size=(2, 2))(x)
    x = SeparableConv2D(6, (3, 3), strides=(1, 1), padding="same", activation="relu")(x)

    # x = ZeroPadding2D(padding=(1, 2))(x)
    # x = DepthwiseConv2D((3, 3), strides=(1, 1), padding="valid", activation=None)(x)
    # x = Conv2D(2, (1, 1), strides=(1, 1), padding="valid", activation=None)(x)
    # x = ReLU()(x)
    # x = BatchNormalization()(x)

    # x = Conv2D(2, (3, 3), strides=(1, 1), padding="valid", activation=None)(x)

    # for i in range(3):
    #     skip_connection = x
    #     x = SeparableConv2D(16, (3, 3), strides=(1, 1), padding="same", activation="relu")(x)
    #     x = SpatialDropout2D(drop)(x)
    #     x = Add()([x, skip_connection])

    # x = MaxPooling2D(pool_size=(2, 2))(x)
    # x = AveragePooling2D(pool_size=(2, 2))(x)
    # x = UpSampling2D(size=(2, 2))(x)
    # x = Dropout(drop)(x)

    # x = ZeroPadding2D(padding=(1, 1))(x)
    # x = SeparableConv2D(32, (3, 3), strides=(1, 1), padding="valid", activation=None)(x)
    # x = LeakyReLU()(x)
    # x = GlobalAveragePooling2D()(x)
    # x = Flatten()(x)
    # x = Dense(16, activation=None, name="dense", kernel_initializer="he_uniform")(x)

    outputs = []
    outputs.append(x)

    model = Model(inputs=inputs, outputs=outputs)
    return model

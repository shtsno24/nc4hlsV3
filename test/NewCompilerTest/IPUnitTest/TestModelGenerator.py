import tensorflow as tf
import numpy as np
from tensorflow.python.client import device_lib
device_list = device_lib.list_local_devices()


def train_model(test_model=None,
                src_data_set=None,
                dst_dataset=None,
                model_file="./keras_model.h5",
                weight_file="./keras_weight.h5"):

    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        # Restrict TensorFlow to only allocate 4GB of memory on the first GPU
        try:
            tf.config.experimental.set_virtual_device_configuration(
                gpus[0],
                [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=4096)])
            logical_gpus = tf.config.experimental.list_logical_devices('GPU')
            print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
        except RuntimeError as e:
            # Virtual devices must be set before GPUs have been initialized
            print(e)

    try:
        with tf.device('/cpu:0'):
            EPOCHS = 1

            # Load dataset
            print("Load dataset...\n\n")
            # train_input, train_output = load_fake_dataset("FakeDatasetTrain.npz")
            train_input, train_output = src_data_set, dst_dataset
            _train_output = []
            for _to in train_output:
                _train_output.append((_to - _to.min()) / (_to.max() - _to.min()))
            train_output = _train_output
            print("\n\nDone")

        # Load model
        print("Load Model...\n\n")
        model = test_model
        model.summary()
        print("\nDone")

        try:
            # Train model
            print("\n\nTrain Model...")
            model.compile(loss=tf.keras.losses.MeanSquaredError(), optimizer='adam', metrics=[tf.keras.metrics.MeanSquaredError()])
            model.fit(train_input, train_output, epochs=EPOCHS)
            print("  Done\n\n")
        except Exception as e:
            print("\n\n", e, "\n\n")
            import traceback
            traceback.print_exc()

        try:
            # Save model
            print("\n\nSave Model...")
            model.save(model_file)
            print("  Done\n\n")

            # Save model
            print("\n\nSave Weights...")
            model.save_weights(weight_file)
            print("  Done\n\n")

            # model.load_weights('param.hdf5')

        except Exception as e:
            print("\n\n", e, "\n\n")
            import traceback
            traceback.print_exc()

    except Exception as e:
        print("\n\n", e, "\n\n")
        import traceback
        traceback.print_exc()
        input(">")

    finally:
        print("Done")

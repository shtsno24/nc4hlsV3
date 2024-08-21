from PIL import Image
import tensorflow as tf
import pathlib
import os
import shutil

if __name__ == "__main__":
    img_output_num = 100
    # img_csv = np.loadtxt('./keras_mnist_DCAE_input_2D.csv', delimiter=", ")
    # img_rescaled = (img_csv - np.min(img_csv)) / (np.max(img_csv) - np.min(img_csv)) * 255

    # img_png = Image.fromarray(img_rescaled.astype(np.uint8))
    # print(img_png.mode)

    # img_png.save('keras_mnist_DCAE_input_2D.png')

    export_dir = "./test_img"

    for i in [export_dir]:
        if os.path.exists(i) is True:
            shutil.rmtree(i)

    for i in [export_dir]:
        p = pathlib.Path(i)
        if p.exists() is False:
            p.mkdir()

    mnist_dataset = tf.keras.datasets.mnist
    (x_train, y_train), (x_test, y_test) = mnist_dataset.load_data()

    for i in range(img_output_num):
        label_num = y_train[i]
        np_ary = x_train[i]
        pil_img = Image.fromarray(np_ary)
        pil_img.save("{}/src_data_{:03}.png".format(export_dir, i))

import numpy as np


def load_fake_dataset():
    with np.load("./FakeDataset.npz") as f:
        print(f.files)
        fake_data_src_0 = f["src_data_0"]
        fake_data_dst_0 = f["dst_data_0"]
    #     fake_data_dst_1 = f["dst_data_1"]
    # return [fake_data_src_0], [fake_data_dst_0, fake_data_dst_1]
    return [fake_data_src_0], [fake_data_dst_0]


def generate_fake_dataset(dtype=np.float32):

    src_height_0 = 28
    src_width_0 = 28
    src_depth_0 = 1

    dst_height_0 = 28
    dst_width_0 = 28
    dst_depth_0 = 6

    # src_height_0 = 64
    # src_width_0 = 64
    # src_depth_0 = 1

    # dst_height_0 = 64
    # dst_width_0 = 64
    # dst_depth_0 = 1

    # dst_height_1 = 1
    # dst_width_1 = 1
    # dst_depth_1 = 2

    len_dataset = 1

    fake_data_src_0 = np.random.rand(len_dataset, src_height_0, src_width_0, src_depth_0).astype(dtype) - 0.5
    fake_data_dst_0 = np.random.rand(len_dataset, dst_height_0, dst_width_0, dst_depth_0).astype(dtype) - 0.5
    # fake_data_dst_1 = np.random.randn(len_dataset, dst_height_1, dst_width_1, dst_depth_1).astype(dtype)
    # np.savez("./FakeDataset.npz",
    #          src_data_0=fake_data_src_0,
    #          dst_data_0=fake_data_dst_0,
    #          dst_data_1=fake_data_dst_1)
    np.savez("./FakeDataset.npz",
             src_data_0=fake_data_src_0,
             dst_data_0=fake_data_dst_0)

    # return ((src_height_0, src_width_0, src_depth_0)), ((dst_height_0, dst_width_0, dst_depth_0), (dst_height_1, dst_width_1, dst_depth_1))
    return ((src_height_0, src_width_0, src_depth_0)), ((dst_height_0, dst_width_0, dst_depth_0))

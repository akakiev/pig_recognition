import preprocessing as ppr
import os

#Parameters
raw_data = '../Data/rawdata'
data_path = '../Data/data'
height = 100
width = 100
if not os.path.exists(data_path):
    ppr.image_processing(raw_data, data_path, height, width)
all_classes = os.listdir(data_path)
print("Classes: {}".format(all_classes))
number_of_classes = len(all_classes)
color_channels = 3
epochs = 1000
batch_size = 10
batch_counter = 0
model_save_name = 'checkpoints/'

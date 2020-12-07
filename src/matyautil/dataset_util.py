import os
import numpy as np
from matyautil.file_util import mkdir, read_txt, write_txt

def split_datalist(datalist, label=None, train_ratio=0.8):
    if type(datalist) is list:
        datalist=np.array(datalist)
    
    data_num=len(datalist)
    train_num=int(data_num*train_ratio)
    id_all   = np.random.choice(data_num, data_num, replace=False)
    id_train  = id_all[0:train_num]
    id_test = id_all[train_num:]
    train_list = datalist[id_train]
    test_list  = datalist[id_test]
    
    if label is not None:
        if type(label) is list:
            label=np.array(label)
        train_label=label[id_train]
        test_label=label[id_train]
        return {"train_list": train_list, "test_list": test_list, "train_label": train_label, "test_label": train_label}

    else:
        return {"train_list": train_list, "test_list": test_list}

def split_txt_datalist(file, save_dir="dataset", train_file_name="train.txt", test_file_name="test.txt"):
    datalist=read_txt(file)
    splitted=split_datalist(datalist)
    mkdir(save_dir)
    write_txt(os.path.join(save_dir,train_file_name), splitted["train_list"])
    write_txt(os.path.join(save_dir,test_file_name), splitted["test_list"])
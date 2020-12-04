import numpy as np
import torch

def tensor2np(x):
    x = x.to('cpu').detach().numpy().copy()
    return x

def np2tensor(x, dtype=np.float32):
    x = torch.from_numpy(x.astype(dtype)).clone()
    return x
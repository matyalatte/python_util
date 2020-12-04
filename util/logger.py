import logging
import os, sys
from .util import mkdir

def setup_logger(name, save_dir="log", filename="log.txt"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    # don't log results for the non-master process

    ch = logging.StreamHandler(stream=sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    mkdir(save_dir)
    fh = logging.FileHandler(os.path.join(save_dir, filename))
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

#sample
#logger=setup_logger("test")
#logger.info("test")

#output
#2020-12-05 03:41:02,646 test INFO: test
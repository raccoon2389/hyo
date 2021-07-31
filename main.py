import os
from aicsimageio import AICSImage
import cv2
import numpy as np
import pandas as pd
from glob import glob
import configparser
import ntpath

def roi(asimg,title):
    img = asimg.get_image_data('TYXZ')
    x,y,w,h = cv2.selectROI(title, img[0], False)

    if w and h:
        r = img[:,y:y+h, x:x+w]
    cv2.waitKey()
    cv2.destroyAllWindows()
    return r

def mean(l):
    return[np.mean(i) for i in l]

if __name__=='__main__':
    config = configparser.ConfigParser()
    config.read('./config.ini')
    czi_path = config['DEFAULT']['CZI_PATH']
    res_path = config['DEFAULT']['RES_PATH']
    if not os.path.exists(res_path):
        os.mkdir(res_path)
    recursive = ('true'== config['DEFAULT']['RECURSIVE'].lower())
    data_path = glob(f"{czi_path}.czi",recursive=recursive)
    t=[i for i in np.arange(-0.3716,20.04782,0.01858)]
     
    key = ['CENTER','BD','WHOLE']
    for path in data_path:
        l=t.copy()
        asimg = AICSImage(path, chunk_dims=["T", "Y", "X"])
        fname = ntpath.basename(path)
        for k in key:
            l.append(mean(roi(asimg,k)))
        pd.DataFrame(l).T.to_excel(f'{res_path}{fname}.xlsx',header=None,index=None)

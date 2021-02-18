import argparse
import numpy as np
import cv2
from os import listdir
from os.path import isfile, join
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
     '--in_path',
     type=str,
     default='./data/input/',
     help='Path to input images folder.')
    parser.add_argument(
     '--out_path',
     type=str,
     default='./data/raw-images/',
     help='Path to raw images folder.')
    args = parser.parse_args()
    myInputPath = args.in_path
    myOutputPath = args.out_path
    allImages = [f for f in listdir(myInputPath) if isfile(join(myInputPath, f))]
    allImages.sort(key = lambda f: int("".join(filter(str.isdigit, f))))
    raw_images = []
    for i in allImages:
     ifile = myInputPath+i
     print(ifile)
    
     ofile = myOutputPath + ifile.split('/')[-1].split('.')[0] + '.raw'
     raw_images.append(ofile.split('/')[-1])
     img = cv2.imread(ifile, cv2.IMREAD_COLOR)
     print (img)
     img = cv2.resize(img, (300, 300))
    
    
     np_arr = np.array(img).astype('float32')
   
     np_arr = np_arr * 0.00784313771874
     
     np_arr = np_arr - 1
    
     np_arr.tofile(ofile)
    with open(myOutputPath+"raw-file.txt", "w") as myfile:
     myfile.write(str("#Postprocessor/BatchMultiClassNonMaxSuppression add")+'\n')
     for rimg in raw_images:
      myfile.write(myOutputPath+rimg+'\n')
    print ('conversion successfull... \n{} images converted in raw images'.format(len(allImages)))

"""usage: python3 conv_frame.py --input_path <path_to_input_parent_directory> --output_path <path_to_output_parent_directory>"""

import cv2
import os
import argparse
fil = []
#oh my gosh
#for conflciting
#hai
parser = argparse.ArgumentParser(description="Convert videos to frames.",
                                     formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument(
        '-i', '--input_path',
        help='Path to the folder where the input video is stored.',
        type=str,
        default=None
    )
parser.add_argument(
        '-o', '--output_path',
        help='Path to the output folder where the images are stored. ',
        type=str,
        default=None
    )
parser.add_argument(
        '-f', '--frame_rate',
        help='Path to the output folder where the images are stored. ',
        type=int,
        default=None
    )
args = parser.parse_args()
for r,d,f in os.walk(args.input_path):
	for files in f:
		fil.append(os.path.join(r,files))
for i in fil:
	print("File",i)
	print()
	cap = cv2.VideoCapture(i)
	basename=os.path.basename(i)
	name=os.path.splitext(basename)[0]
	count = 0
	file_count = 1
	out=os.path.join(args.output_path,name)
	os.mkdir(out)
	while cap.isOpened():
		ret, frame = cap.read()
		if ret:
			cv2.imwrite(os.path.join(out,name + "_" + '{:d}.jpg'.format(file_count)), frame)
			count += args.frame_rate
			cap.set(1, count)
			print("Extracting the frames",file_count,"Continues")
			file_count = file_count+1
		else:
			cap.release()
			break
			print("Outputs stored to:=====>",out)

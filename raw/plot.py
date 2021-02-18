# Python program to explain cv2.rectangle() method 

# importing cv2 
import cv2 

#path
file2 = open("/home/vkchcp0113/INSU_AIML/Jishnu/board_exp/conversion/result/dsp.txt","r")
file1 = open("/media/vkchcp0113/New_Volume/INSU_AIML/obj_det/dataset/animal_person_package_12_01/train_test/raw_img/raw-file.txt","r")
#image = cv2.imread(path)
#image = cv2.resize(image,(300,300)) 


"""coco = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'street sign', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'hat', 'backpack', 'umbrella', 'shoe', 'eye glasses', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'plate', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'mirror', 'dining table', 'window', 'desk', 'toilet', 'door', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'blender', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush', 'hair brush']"""
coco = ['animal','person','package']

window_name = 'Image'
# font 
font = cv2.FONT_HERSHEY_SIMPLEX 
  
# org 
org = (50, 50) 
  
# fontScale 
fontScale = 0.5
   
# Blue color in BGR 
color = (255, 0, 0) 
  
# Line thickness of 2 px 
thickness = 2
i =0
count = 0
flag = 1
for l in file1:
	#i+=1
	if "raw" in l:
		#print("line_in_rawfile.txt",l)
		l = l.split(".")
		#print(l)
		nam = l[0]
		name = nam + ".jpg"
		print(name)
		img = cv2.imread(name)
		#print(img)
		img = cv2.resize(img,(300,300)) 
		file2 = open("/home/vkchcp0113/INSU_AIML/Jishnu/board_exp/conversion/result/dsp.txt","r")
		count = -1
		for line in file2:
			#print("line_in_framefile",line)
			if "frame" in line:
				count+=1
				print("###################################################",count,i)
			if(count==i and "frame" not in line):
				#print("hi")
			
				line1 = line.split(" ")
				ymin = int(float(line1[0])*300)
				#print xmin
				xmin = int(float(line1[1])*300)
				ymax = int(float(line1[2])*300)
				xmax = int(float(line1[3])*300)
				cls = line1[4]
				print(type(cls))
				clss = coco[int(float(cls))-1]
	
				print(clss)	
				conf = line1[5]
	
			
	
		# represents the top left corner of rectangle 
				start_point = (xmin,ymin ) 

	
		# represents the bottom right corner of rectangle 
				end_point = (xmax ,ymax) 

		# Blue color in BGR 
				color = (255, 0, 0) 

		# Line thickness of 2 px 
				thickness = 1

		# Using cv2.rectangle() method 
		# Draw a rectangle with blue line borders of thickness of 2 px 
				image = cv2.rectangle(img, start_point, end_point, color, thickness)
				name = str(conf) + " " + str(clss)
				cv2.putText(image, name, (xmin -5 ,ymin- 5), font, fontScale, color, thickness, cv2.LINE_AA) 
			
		# Displaying the image
				imgnam = "/media/vkchcp0113/New_Volume/INSU_AIML/obj_det/dataset/animal_person_package_12_01/train_test/result/frame_" + str(i) + ".jpg" 
				cv2.imwrite(imgnam, image)
		file2.close() 
		i+=1
		print("hilt")


import numpy as np
import cv2



path = "/home/vkchcp0113/INSU_AIML/Jishnu/board_exp/conversion/result/output_dsp/Result_"
k = 0
threshold = 0.7
while(1):
	res1 = np.fromfile(path +str(k)+'/Postprocessor/BatchMultiClassNonMaxSuppression_scores.raw', dtype="float32")
	#print(res1)
	#print("#######################################################################")
	res2 = np.fromfile(path + str(k)+'/detection_classes:0.raw', dtype="float32")
	#print(res2)
	print("#######################################################################")
	res3 = np.fromfile(path+str(k)+'/Postprocessor/BatchMultiClassNonMaxSuppression_boxes.raw', dtype="float32")
	print(res3)


	
	with open("/home/vkchcp0113/INSU_AIML/Jishnu/board_exp/conversion/result/dsp.txt", "a") as f1:
		f1.write("frame_"+str(k)+"\n")
		for i in range (0,len(res3)):
			if (i%4 == 0):
	
				line = str(res3[i]) + " " +str(res3[i+1]) + " " +str(res3[i+2]) + " " + str(res3[i+3]) + " " +str(res2[i//4]) +" " +str(res1[i//4])+"\n"
				if(res1[i//4] > threshold):
					
					f1.write(line)
	k+=1


# -*- coding: utf-8 -*-
import cv2
import glob
import json
import numpy as np
import os
import subprocess
from subprocess import call





def check_folder(path_to_file, extention):
	cv_img = []
	there_files = False
	path = path_to_file
	for img in glob.glob("{}*.{}".format(path,extention)):
	    n = cv2.imread(img)
	    cv_img.append(n)
	if len(cv_img) != 0:
		#print(cv_img)
		print('Folder not empty, folder len is ..', len(cv_img))
		there_files = True
		return there_files
	else:
		print('No files in {}!!'.format(path_to_file))
		return False



def get_plates(result):
	plates = result['candidates'][0]
	return plates
	#print(plates)


def get_plate_region(result):
	region = result['coordinates'][0]
	return region

#from pandas.io.json import json_normalize

def get_json_from_api(image):

	print(image)
	cmd = ['curl','X', 'POST', '-F','image=@{}'.format(image),'https://api.openalpr.com/v2/recognize?recognize_vehicle=1&country=us&secret_key=sk_DEMODEMODEMODEMODEMODEMO']
	
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	out, err= p.communicate()
	out = out.decode('utf-8')

	m = out
	n = json.dumps(m)  
	o = json.loads(n)  
	return str(o)

def read_data(img_glob):
	files = []
	for fname in sorted(glob.glob(img_glob)):
		print('...',fname)

		#img = cv2.imread(fname)[:, :, 0].astype(np.float32) / 255.
		img = cv2.imread(fname)

	##############################################
	# HER LEFT TO CHABNGE BITWHISECHANGE FROM BGR TO RGB in img
	####################################
		date = fname.split("/")[1][0:18]

		code = fname.split("/")[1][-13:-4]

		files.append([fname,img,code,date])
		#os.remove(fname)

	return files
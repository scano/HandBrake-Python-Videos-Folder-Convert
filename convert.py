#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import traceback
import os
import io
import subprocess
import glob
import json

if len(sys.argv) < 3:
	print('\nPass the HandBrake exported preset JSON file and the source folder as argument.\nEx: convert.py H264-1080-3800K.json  /Volumes/Data/My Videos\n')
	exit()

preset_file = sys.argv[1]
root_dir = glob.escape(sys.argv[2])
current_dir=os.path.dirname(os.path.realpath(__file__))

preset_json = json.load(open(preset_file))
preset_name = preset_json['PresetList'][0]['PresetName']

# root_dir needs a trailing slash (i.e. /root/dir/)
for file_in in sorted(glob.iglob(root_dir + '/**/*.*', recursive=True)):
	
	if not file_in.endswith(tuple(["mp4", "mkv", "avi", "mov"])) or "__" in file_in:
		print('⚠️ Skiping ', file_in)
		continue
		
	print('⚡️ Procesing ', file_in)
	 
	file_out = file_in.replace('.', '__.')
	file_out = file_out.split('.')[0] + '.mp4'
	
	cmd = f"HandBrakeCli --preset-import-file '{preset_file}' -Z '{preset_name}' -i '{file_in}' -o '{file_out}'"
	#print(cmd)
	
	process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	log = ""
	for line in io.TextIOWrapper(process.stdout, encoding="utf-8"):
		if 'Encoding' in line:
			line = line.replace('\n','')
			print(f"{file_out} → {line}", end="\r")
		else:
			log += line
	
	print("\n")
	return_code = process.poll()

	if return_code > 0:
		print(f"❌ Unable to process {file_in}\n")
		print("INI ERROR ======================================================")
		print(log)
		print("END ERROR ======================================================\n")
	else:
		try:
			os.remove(file_in)
			os.rename(file_out, file_out.replace('__.','.'))
			print(f"✅ {file_in} done!")
		except:
			pass
	

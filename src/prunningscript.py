# -*- coding: utf-8 -*-

import sys
import codecs
import re
import os
import pickle
import json

#python prunningscript.py chunk_list phrase-table_file
file_i = sys.argv[2]

list=[]

delete_file = open("../data/deleted","w")
hindi_dataset = open("../data/check.hi","w")
english_dataset = open("../data/check.en","w")


for i in codecs.open(sys.argv[1]):
	list.append(i.strip())

list = set(list)
print(len(list))
print("%" in list)
count = 0
f1 = open("../data/prunned_phrase_table.hi-en", "w")

for i in codecs.open(file_i):
	#extracting hindi phrase from the phrase table
	j=i.strip().split('|||')
	hindi = j[0].strip()
	#if hindi phrase is only "'" then do not include it into the dataset
	if hindi == "'":
		count+=1
		delete_file.write(i)

	elif hindi in list:
		f1.write(i.strip() + "\n")

	# elif hindi in list:
	# 	#If hindi phrase extracted is in the chunk list then inlcude in the dataset.
	# 	hindi_dataset.write(hindi)
	# 	hindi_dataset.write("\n")

	# 	#writing english phrase to the English file

	# 	english_dataset.write(j[1].strip())
	# 	english_dataset.write("\n")

	# else:
	# 	with open("../data/prunned","a") as f:
	# 		f.write(j[0].strip()+"\n")

f1.close()
print(count)

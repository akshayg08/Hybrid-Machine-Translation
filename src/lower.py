import sys

file = sys.argv[1]
temp = file.split(".")
out_file = ".".join(temp[:-1])+".lower." + temp[-1]

f1 = open(out_file, "w")

with open(file) as f:
	for line in f:
		f1.write(line.strip().lower() + "\n")

f1.close()

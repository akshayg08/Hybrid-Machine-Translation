f1 = open("../phrase-table.hi-en.onmt", "w")

with open("../phrase-table.hi-en") as f:
	for line in f:
		temp = line.split("|||")
		source = temp[0].strip()
		target = temp[1].strip()
		f1.write(source+"|||"+target+"\n")

f1.close()	

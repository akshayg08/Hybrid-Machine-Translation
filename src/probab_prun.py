f1 = open("../prob/prunned2.fr-en", "w")

with open("../phrase-table") as f:
	for line in f:
		temp = line.strip().split(" ||| ")
		source = temp[0]
		target = temp[1]
		scores = temp[2]
		direct_phrase_translation_probability = float(scores.split()[2].strip())
		if direct_phrase_translation_probability >= 0.9:
			f1.write(source+"|||"+target+"\n")

f1.close()

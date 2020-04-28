data = []
with open("../phrase-table.hi-en") as f:
	for line in f:
		temp = line.strip().split(" ||| ")
		scores = temp[2]
		direct_phrase_translation_probability = float(scores.split()[2].strip())
		data.append((direct_phrase_translation_probability, line))

data.sort()
with open("../sorted_phrase_table.hi-en", "w") as f:
	for line in data[::-1]:
		f.write(line[1].strip() + "\n")

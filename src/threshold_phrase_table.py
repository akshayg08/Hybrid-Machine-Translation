import sys
import pickle

uniq = {}
prob = {}

inp = sys.argv[1]
thresh = float(sys.argv[2])
out = "threshold_" + str(thresh) + "_" + inp+".pkl"

with open(inp) as f:
	for line in f:
		temp = line.strip().split(" ||| ")
		scores = temp[2]
		src = temp[0].strip()
		trg = temp[1].strip()
		direct_phrase_translation_probability = float(scores.split()[2].strip())
		# data.append((direct_phrase_translation_probability, line))
		if direct_phrase_translation_probability >= thresh:
			if src not in uniq:
				uniq[src] = trg
				prob[src] = direct_phrase_translation_probability
			else:
				if direct_phrase_translation_probability > prob[src]:
					uniq[src] = trg
					prob[src] = direct_phrase_translation_probability

pickle.dump(uniq, open(out, "wb"))

# data.sort()
# with open(out, "w") as f:
# 	for line in data[::-1]:
# 		if float(line[0]) >= thresh:
# 			f.write(line[1].strip() + "\n")

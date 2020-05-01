import pickle
chunks = {}

prev = ""
words = []

with open("../chunk_features_with_predicted_chunk_tag") as f:
	for line in f:
		tp = line.strip().split()
		if len(tp) < 2:
			continue
		chunk_tag = tp[2].strip()
		word = tp[0].strip()
		temp = chunk_tag.split("-")[0].strip()

		if prev == "" and temp == "B":
			words.append(word)
			prev = "B"

		elif prev != "" and temp == "I":
			words.append(word)
			prev = "I"

		elif prev != "" and temp == "B":
			chunk = " ".join(words)
			chunks[chunk] = 1
			words = [word]
			prev = "B"

pickle.dump(chunks, open("../data/chunk_list.pkl", "wb"))

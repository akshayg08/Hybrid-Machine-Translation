import pickle	

chunks = pickle.load(open("../data/chunk_list.pkl", "rb"))
phrases = pickle.load(open("../data/threshold_0.0_phrase-table.pkl", "rb"))

print(len(phrases))
temp = list(phrases.keys())

for phrase in temp:
	if phrase not in chunks:
		del phrases[phrase]

print(len(phrases))
pickle.dump(phrases, open("../data/prunned_phrase_table.pkl", "wb"))

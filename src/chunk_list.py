with open("../data/training/new_train_prun_chunks.hi") as f:
	data = f.readlines()

chunk_list = {}

for line in data:
	chunks = line.strip().split()
	for chunk in chunks:
		temp = " ".join(chunk.split("_"))
		if temp not in chunk_list:
			chunk_list[temp] = 1

with open("../data/training/hindi_chunk_list.txt", "w") as f:
	for chunk in chunk_list.keys():
		f.write(chunk.strip() + "\n")

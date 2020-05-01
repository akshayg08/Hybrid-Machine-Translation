with open("../data/train.hi") as f:
	train_hi = f.readlines()

with open("../data/train.en") as f:
	train_en = f.readlines()

with open("../data/dev.hi") as f:
	dev_hi = f.readlines()

with open("../data/dev.en") as f:
	dev_en = f.readlines()

with open("../data/test.hi") as f:
	test_hi = f.readlines()

with open("../data/test.en") as f:
	test_en = f.readlines()

hi = []
en = []

hi += train_hi
hi += dev_hi
hi += test_hi
en += train_en
en += dev_en
en += test_en






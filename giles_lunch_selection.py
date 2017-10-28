from random import shuffle

def random_selection(filename, num):
	with open(filename) as f:
		content = f.readlines()
	candidates = [x.strip('\n') for x in content]
	shuffle(candidates)
	for candidate in candidates[:num]:
		print candidate, "has been chosen for the event!"

if __name__ == '__main__':
	filename = raw_input("Enter filename: ").strip()
	num = raw_input("How many people will be attending? ").strip()
	random_selection(filename, int(num))
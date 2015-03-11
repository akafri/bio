from configuration import *
import jellyfish_wrapper

def count_all():
	for species in species_url_path.keys():
		for chromo in range(1, species_cnt[species] + 1):
			for k in k_range:
				print("count all: {0}, {1}, {2}".format(species, chromo, k))
				jellyfish_wrapper.count(k, 
				      repo_fa_path.format(fa_file_format.format(species, chromo)), 
				      repo_mer_path.format(mer_file_format.format(species, chromo, k)))


def main():
	count_all()


if __name__ == '__main__':
	main()

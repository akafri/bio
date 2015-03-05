#!/usr/bin/python

import os
import logging

download_cmd = 	"wget --timestamping ftp://hgdownload.cse.ucsc.edu/goldenPath/{0}/chromosomes/chr{1}.fa.gz -O {2}_chr{3}.fa.gz"

species_url_path = {'human':'hg19', 'mouse': 'mm10'}
species_cnt = {'human':22, 'mouse': 19}

def download_fa_file(species, chr_id):
	logging.info("download_fa_file: {0}, {1}".format(species, chr_id))
	os.system(download_cmd.format(species_url_path[species], chr_id, species, chr_id))

def download_all_fa():
	for species in species_url_path.keys():
		for chr_id in range(1, species_cnt[species] + 1):
			download_fa_file(species, chr_id)


def main():
	download_all_fa()



if __name__ == '__main__':
	main()

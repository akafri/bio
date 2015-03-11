#!/usr/bin/python

import os
import logging
from configuration import *


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

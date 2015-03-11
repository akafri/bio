from download_chromosomes import *

import os


jellyfish_count_cmd = 'jellyfish count -m {0} -s 1G -t 16 {1} -o {2}'

def count(k, fa_file, output_mer_file):
	os.system(jellyfish_count_cmd.format(k, fa_file, output_mer_file)) 


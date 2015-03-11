download_cmd =  "wget --timestamping ftp://hgdownload.cse.ucsc.edu/goldenPath/{0}/chromosomes/chr{1}.fa.gz -O {2}_chr{3}.fa.gz"

species_url_path = {'human':'hg19', 'mouse': 'mm10'}
species_cnt = {'human':22, 'mouse': 19}

k_range = range(1, 13)
fa_file_format = '{0}_chr{1}.fa'
mer_file_format = '{0}_chr{1}_{2}.jf'
repo_fa_path = '/home/akafri/bio/repo/chromosome_files/fa/{0}'
repo_mer_path = '/home/akafri/bio/repo/chromosome_files/mer/{0}'

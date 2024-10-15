import pandas as pd

# Load the dictionary file (gene_dic.dat)
gene_dict = pd.read_csv('gene_dic.dat.txt', sep='\t', header=None, names=[
    'Affymetrix_ID', 'Chromosome', 'Index', 'SNP0', 'SNP1', 'SNP2', 'SNP3'], lo$

# Display first few rows
print(gene_dict.head())

# Parse the SNP data file
def parse_snp_file(snp_file):
    with open(snp_file, 'r') as file:
        for line in file:
            eid = line[:7].strip()  # Extract the 7-digit EID
            snps = line[7:].strip()  # Extract SNPs for this individual
            yield eid, snps

# Example: Parse the rand_chr21.dat
snp_data = list(parse_snp_file('rand_chr22.dat'))

# Display first SNP data
print(snp_data[:3])

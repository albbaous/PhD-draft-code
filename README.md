# PhD-draft-code
Just a repo where I can walk myself through my process 

### Synthetic data download
``https://biobank.ndph.ox.ac.uk/synthetic_dataset/ ``
    - Downloaded the files `gene_dic.dat.txt` and `rand_chr22.dat`
    - We have a dictionary file (e.g., gene_dic.dat) that maps SNP indices to their actual genotype variants, and genotype data files (e.g., rand_chr*.dat.gz) with SNP values for individuals.
    
### Installing dependencies on my practice conda environment 

```bash
conda install numpy pandas matplotlib seaborn scikit-learn scipy keras
conda install -c pytorch pytorch torchvision torchaudio
conda install -c conda-forge xgboost lightgbm statsmodels
```

- `tensorflow` was being weird so i left it for now

### Parse the SNP Data
- Parsing the SNP data, using the dictionary file (gene_dic.dat) to map SNP indices to actual SNP variants. This uses `parse_snp.py`
- using HPC so run it using `run.bash`

### Genotype Data Preprocessing
0: Homozygous reference (e.g., "C C")
1: Heterozygous (e.g., "T C")
2: Homozygous alternative (e.g., "T T")

We want to combine the SNP data for all chromosomes to create a full matrix of individuals × SNPs - in this case, i have one chromosome though - might incorporate this later

Missing data (represented by NaN) can be imputed using methods such as:
#### Mean imputation: 
Replace NaNs with the most common genotype (e.g., mode) for that SNP.
#### KNN imputation (I am gonna attempt this) : 
Use the nearest neighbors to impute missing values based on similar individuals.

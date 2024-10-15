# PhD-draft-code
Just a repo where I can walk myself through my process 

### Synthetic data download
``https://biobank.ndph.ox.ac.uk/synthetic_dataset/ ``
    - Downloaded the files `gene_dic.dat.txt` and `rand_chr22.dat`
    
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

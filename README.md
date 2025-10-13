# Hominin mtDNA Kallisto Pipeline

This pipeline runs on a folder with BAM-files and creates a kallisto-plot similar to the one created by Vernot et al. 2021 (and the data-files for custom plotting) 
 
![](assets/example.png)

## Requirements

- singularity
- nextflow v22.10 (or larger)

## Usage

```
NXF_VER=24.04.4 nextflow run merszym/kallisto_nf -r v0.1 --split INPUT-DIR -profile PROFILE
```

INPUT-DIR is a directory containing BAM-files (e.g. unique or deaminated sequences, mapped to the human mtDNA reference genome)

## Profiles

### Hominidae

Use the `-profile Hominidae` flag to use the included human mtDNA reference panel. See the content in the [Labels](assets/Hominidae/labels.tsv)

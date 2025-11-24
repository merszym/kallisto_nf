# Sedimentary mtDNA Kallisto Pipeline

Many sedaDNA libraries are not suitable for reconstructing (e.g hominin) mtDNA consensus sequences, because they contain too few mtDNA fragments or the data comes from multiple populations in the same layer. Kallisto (Bray et al. 2016) is a kmer-based method that can be used to estimate the affinity of a set of DNA sequences to a provided mtDNA reference panel. 

This pipeline presents a simple workflow for the analysis of sedimentary ancient DNA using Kallisto, as presented by Vernot et al. 2021.

Given a folder with pre-filtered BAM or FASTQ files (e.g. unique Hominin mtDNA sequences), this pipeline produces a kallisto-plot, the mtDNA abundance proportions and raw kallisto files for custom processing.   

> [!NOTE]
> At the moment, we only support the Human mtDNA analysis, but we plan to extend the project to other mammalian families as well.
 
## Requirements

- singularity
- nextflow v22.10 (or larger)

## quickstart

To test how the pipeline works, download the human mtDNA sequences from Satsurblia Cave sample SAT29, published in Gelabert et al. 2021 from the European Nucleotide Archive (ENA)

```
wget -P split ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR601/004/ERR6016624/ERR6016624.fastq.gz
wget -P split ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR601/008/ERR6016628/ERR6016628.fastq.gz

NXF_VER=24.04.4 nextflow run merszym/kallisto_nf --split split/ -profile Hominidae
```

### Example Output 

The pipeline produces a heat-map showing the relative mtDNA abundance estimates for the sequences in each file. 

![](assets/quickstart_example.svg)

## Usage

```
NXF_VER=24.04.4 nextflow run merszym/kallisto_nf -r v0.1 --split INPUT-DIR -profile PROFILE
```

INPUT-DIR is a directory containing BAM- or FASTQ-files (e.g. unique or deaminated sequences, mapped to the human mtDNA reference genome)

## Profiles

### Hominidae

Use the `-profile Hominidae` flag to use the included human mtDNA reference panel as used by Zavala et al. 2021 and Vernot et al. 2021. See the content of the reference panel in the [Labels](assets/Hominidae/labels.tsv). 

### Hyaenidae

Use the `-profile Hyaenidae` flag to use the included hyaenidae mtDNA reference panel. See the content of the reference panel in the [Labels](assets/Hyaenidae/labels.tsv).

### Ursidae

Use the `-profile Ursidae` flag to use the included Ursidae mtDNA reference panel. See the content of the reference panel in the [Labels](assets/Ursidae/labels.tsv).

### Cervidae

Use the `-profile Cervidae` flag to use the included Cervidae mtDNA reference panel. See the content of the reference panel in the [Labels](assets/Cervidae/labels.tsv).

## Kallisto index

Kallisto index was created with 
```
singularity exec https://depot.galaxyproject.org/singularity/kallisto:0.44.0--h7d86c95_2 kallisto index -k 21 -i GROUP_k21.idx GENOMES.fa
```

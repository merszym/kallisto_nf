# Sedimentary mtDNA Kallisto Pipeline

Many sedaDNA libraries are not suitable for reconstructing (e.g hominin) mtDNA consensus sequences, because they contain too few mtDNA fragments or the data comes from multiple populations in the same layer. Kallisto (Bray et al. 2016) is a kmer-based method that can be used to estimate the affinity of a set of DNA sequences to a provided mtDNA reference panel. 

This pipeline presents a simple workflow for the analysis of sedimentary ancient DNA using Kallisto, as presented by Vernot et al. 2021.

Given a folder with pre-filtered BAM or FASTQ files (e.g. unique Hominin mtDNA sequences), this pipeline produces a kallisto-plot, the mtDNA abundance proportions and raw kallisto files for custom processing.   

> [!NOTE]
> At the moment, we only support the Human mtDNA analysis, but we plan to extend the project to other mammalian families as well.
 
## Requirements

- singularity
- nextflow v22.10 (or larger)

## Usage

```
NXF_VER=24.04.4 nextflow run merszym/kallisto_nf --split INPUT-DIR -profile PROFILE
```

INPUT-DIR is a directory containing BAM- or FASTQ-files (e.g. unique or deaminated sequences, mapped to the human mtDNA reference genome)

**Flags**
```
--trim           N       Trim N bases on each end of DNA reads before running kallisto (default: 3)
--kallisto_mask  N       Mask any assignment lower than N 'est_counts' from the kallisto-plot (default: 25). Decrease for low coverage data
--outdir         STRING  Custom name for output directory

```

### Example Output 

The pipeline produces a heat-map showing the relative mtDNA abundance estimates for the sequences in each BAM file. 

![](assets/DC_MainChamber.svg)

The example shows the plot for sediment DNA data generated from Denisova Cave and published in Zavala et al. 2021. Human mtDNA sequences were separated from the faunal components using quicksand v2.3. As published, the plot shows the population turnover within the Denisovans and the Neanderthals. Within the modern humans kallisto is less precise (and requires further tests)

## Profiles

### Hominidae

Use the `-profile Hominidae` flag to use the included human mtDNA reference panel, consisting of Denisovans, Neanderthals and Modern Humans. See the content of the reference panel in the [Labels](assets/Hominidae/labels.tsv). 

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

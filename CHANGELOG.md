# Change Log

All notable changes to this project will be documented in this file.

## [v1.1]

### Updated Workflow
- Added fastp to pre-filter reads prior to quantification. Implemented fastp with the --dedup and the --low_complexity_filter and --complexity_threshold 50 flags to remove exact read duplicates and low-complexity sequences.

### Reference genomes updates
- Ursidae: Added Middle Pleistocene mtDNA genomes
- Canidae: Added Bergström et al. 2022 Canis lupus genomes and Taron et al. 2021 ancient Cuon genomes
- Felidae: Replaced genomes that were contaminated by NUMTS
 
### Removed low complexity regions
Based on a MSA of the reference genomes, we removed low-complexity regions with many gaps and Ns in the
reference panel:

- Canidae:
    - Positions 16099-16687 based on Speothos venaticus (MW257226.1)
- Felidae
    - Positions 259 - 668 based on Panthera pardus (NC_010641.1)

### Added 'sinks'
Added sequences and genomes to databases that are not tracked in the 'labels' to 'catch' sequences that are not of mitochondrial origin OR contamination from other families. These sinks are:

1. A few mtDNA genomes of other families (mostly hyena)
2. nuclear sequences that look like mtDNA (NUMTS) for the Carnivora. 

More specifically: 

- Ursidae: Added Hyaenidae and Canidae genomes: MN320460.1, EU408260.1
- Canidae: Added Ursidae, Hyaenidae and Mustelidae genomes: AF303110.1, MN320460.1, NC_020644.1 
- Felidae: Added Hyaenidae genome: MN320460.1

To Felidae, Ursidae, Canidae, Hyaenidae: All NUMTS sequences of that family, as published in [Liu et al. 2025](https://doi.org/10.1093/gbe/evaf174).

## [v1.0]

Lots of accumulated (and undocumented) changes to profiles/databases. So now with a fresh version number!

### Changes
#### Workflow
- Adds bowtie2 as a filter before kallisto-quantification. Only sequences that map to at least 1 of the genomes in the reference-panel are selected for kallisto quant to reduce false-positive rate
- Set the default `maxlen` parameter to 150. 

#### References/Profiles
- Removes the profile `Ovis`
- Adds the profiles `Bovidae`,`Elephantidae`,`Equidae`,`Felidae`,`Rhinocerotidae`,`Ursidae`
- Updates all other profiles

## [v0.4]

### Changes
- Adds profile `Canidae`

## [v0.3]

Very exploratory version, mostly updates of the underlying databases

### Changes
- Adds profiles `Ursidae`,`Cervidae` and `Ovis`
- Updates `Hominidae` reference database
- Add max-length (`--maxlen`) and trimming (`--trim`) parameter 
- Add filters for the kallisto-plot (>=10% of the counts, >=25 estimated reads)
- Add lines to Kallisto-heatmap (species and haplogroups)

## [v0.2]

### Changes

- Use profiles to specify which set of references to use. `-profile Hominidae` 
- Add Hyaenidae reference-panel, use with `-profile Hyaenidae` 

### Bugfixes
# Change Log

All notable changes to this project will be documented in this file.

## [v1.1]

### Reference genomes updates
- Ursidae: Added Middle Pleistocene mtDNA genomes
- Canidae: Added Bergström et al. 2022 Canis lupus genomes
 
### Removed low complexity regions
Based on a MSA of the reference genomes, we removed low-complexity regions with many gaps and Ns in the
reference panel:

- Canidae:
    - Positions 16099-16687 based on Speothos venaticus (MW257226.1)
- Felidae:
    - Positions 259 - 668 based on Panthera pardus (NC_010641.1)

### Added 'sinks'
Added outgroup-genomes to databases to avoid the assignment of root-clades due to missing references.

- Ursidae: Added Hyaenidae and Canidae genomes: MN320460.1, EU408260.1
- Canidae: Added Ursidae, Hyaenidae and Mustelidae genomes: AF303110.1, MN320460.1, NC_020644.1 

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
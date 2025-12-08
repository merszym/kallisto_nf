# Change Log

All notable changes to this project will be documented in this file.

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
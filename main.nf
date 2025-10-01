// Import modules

include { SAMTOOLS_FASTQ     } from './modules/local/samtools_fastq'
include { KALLISTO_QUANT     } from './modules/local/kallisto_quant'
include { SUMMARIZE_KALLISTO } from './modules/local/summarize'

// load the files

ch_split     = Channel.fromPath("${params.split}/*"  ,checkIfExists:true) // input-data
ch_database  = Channel.fromPath("${params.database}" ,checkIfExists:true) // kallisto-index
ch_versions = Channel.empty()

// some required functions
def has_ending(file, extension){
    return extension.any{ file.toString().toLowerCase().endsWith(it) }
}

//
// MAIN WORKFLOW
//

workflow {

// add a first meta
ch_split.map{it -> [['sample': it.baseName, 'id':it.baseName], it] }.set{ ch_split }

//split input into bam- and fastq-files
ch_split.branch {
    bam: it[1].getExtension() == 'bam' //input BAMS need to be converted to fastq-files
    fastq: has_ending( it[1], ["fastq","fastq.gz","fq","fq.gz"])
    fail: true
}
.set{ ch_split }

//
// 0. BAM to Fastq
//

SAMTOOLS_FASTQ(ch_split.bam)

ch_versions = ch_versions.mix(SAMTOOLS_FASTQ.out.versions.first())
ch_converted_fastq = SAMTOOLS_FASTQ.out.fastq

ch_split_fastq = ch_split.fastq.mix(ch_converted_fastq)


//
// 1. Run KALLISTO
//

ch_for_kallisto = ch_split_fastq.combine(ch_database)

KALLISTO_QUANT(ch_for_kallisto)

ch_tsv = KALLISTO_QUANT.out.tsv
ch_tsv.map{ meta, tsv -> 
    def abundance = tsv.splitCsv(sep:'\t', header:true) // first because the splitCsv results in [[key:value]]
    [
        meta,
        abundance
    ]
}
.transpose()
.map{meta, row -> meta+row }
.set{ ch_final }

ch_final.collect()
    .map{it -> 
        def header = it[0].keySet().join('\t')
        def lines = it.collect { row -> row.values().join('\t') }
        ([header] + lines).join('\n')
    }
    .set{ ch_summary }


ch_summary.collectFile(name:'kallisto_summary.tsv', storeDir:'.' )

//
// 2. Create Kallisto-Plots and sheets
//

SUMMARIZE_KALLISTO(ch_summary.collectFile(name:'kallisto_summary.tsv'))

}


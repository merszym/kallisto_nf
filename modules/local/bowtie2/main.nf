process BOWTIE2 {
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/bowtie2:2.5.4--he96a11b_5' :
        'quay.io/biocontainers/bowtie2:2.5.4--he96a11b_5' }"
    tag "$meta.id"

    input:
    tuple val(meta), path(fastq), path(bowtie_index)

    output:
    tuple val(meta), path("${meta.id}.fq.gz"), emit: fq
    path "versions.yml"                      , emit: versions

    script:
    """
    bowtie2 -x ${bowtie_index}/${meta.bowtie2_name} -U ${fastq} --al-gz ${meta.id}.fq.gz > /dev/null

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        bowtie: \$(bowtie2 version | head -1 | cut -d' ' -f3)
    END_VERSIONS
    """
}
process SEQTK_TRIMFQ {
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/seqtk:1.5--h577a1d6_1' :
        'quay.io/biocontainers/seqtk:1.5--h577a1d6_1' }"
    tag "$meta.id"

    input:
    tuple val(meta), path(fastq)

    output:
    tuple val(meta), path("${meta.id}_trimmed.fq"), emit: fastq
    path "versions.yml"                           , emit: versions

    script:
    """
    seqtk trimfq -b ${params.trim} -e ${params.trim} ${fastq} > ${meta.id}_trimmed.fq

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        seqtk: \$(seqtk 2>&1 | head -3 | tail -1)
    END_VERSIONS
    """
}
process KALLISTO_QUANT {
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/kallisto:0.44.0--h7d86c95_2' :
        'quay.io/biocontainers/kallisto:0.44.0--h7d86c95_2' }"
    tag "$meta.id"

    input:
    tuple val(meta), path(fastq), path(database)

    output:
    tuple val(meta), path("abundance.tsv")  , emit: tsv
    tuple val(meta), path("*.{h5,tsv,json}"), emit: data
    path "versions.yml"                     , emit: versions

    script:
    """
    kallisto quant -b100 --single -i ${database} -l 50 -s 10 -o . ${fastq}

    cat <<-END_VERSIONS > versions.yml
    "${task.process}":
        kallisto: \$(kallisto | head -n1 | cut -d ' ' -f2)
    END_VERSIONS
    """
}
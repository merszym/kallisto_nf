process FASTP_DEDUP {
    container "${ workflow.containerEngine == 'singularity' && !task.ext.singularity_pull_docker_container ?
        'https://depot.galaxyproject.org/singularity/fastp:0.24.0--heae3180_1' :
        'quay.io/biocontainers/fastp:0.24.0--heae3180_1' }"

    input:
        tuple val(meta), path(fastq)

    output:
        tuple val(meta), path("${meta.id}_dedup.fastq"), emit: fastq


    script:
    """
    fastp -i ${fastq} -o ${meta.id}_dedup.fastq --dedup --low_complexity_filter --complexity_threshold 50 
    """  

}
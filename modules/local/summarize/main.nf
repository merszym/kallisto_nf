process SUMMARIZE_KALLISTO{
    container (workflow.containerEngine ? "merszym/pandas_seaborn:nextflow" : null)
    tag "Plotting"
    label 'local'

    input:
    path(tsv)
    path(labels)

    output:
    path("*")

    script:
    """
    postprocessing.py ${tsv} ${labels}
    """
}
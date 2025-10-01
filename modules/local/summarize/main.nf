process SUMMARIZE_KALLISTO{
    container (workflow.containerEngine ? "merszym/pandas_seaborn:nextflow" : null)
    tag "Plotting"
    label 'local'

    input:
    val(tsv)

    output:
    path("*")

    script:
    """
    postprocessing.py ${tsv}
    postprocessing.py ${tsv} archaics
    """
}
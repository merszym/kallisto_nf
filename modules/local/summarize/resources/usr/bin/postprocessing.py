#! /usr/bin/env python3

from pathlib import Path
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt


def summarize_kallisto(tsv, mode):

    kallisto = pd.read_csv(tsv, sep='\t')

    # sort columns
    cols = [
        "rCRS_NC_012920",
        "AF347008",
        "AF346999",
        "AF381988",
        "AY195766",
        "AF381981",
        "AF346995",
        "AF346977",
        "AY289097",
        "AY289082",
        "AY289085",
        "DQ137410",
        "DQ137411",
        "AF347015",
        "AY195759",
        "AF347014",
        "AF381998",
        "AY950293",
        "AY950300",
        "AF346973",
        "AF381996",
        "AF381984",
        "AF347010",
        "AY963573",
        "AF346990",
        "AY195748",
        "AF346966",
        "AY289059",
        "AY195756",
        "AF381999",
        "AY882393",
        "AY882380",
        "AY195754",
        "AY195774",
        "AY963586",
        "AY882382",
        "AY963572",
        "AY195787",
        "AY195773",
        "AF382000",
        "AY882392",
        "AY882391",
        "AY882412",
        "AY882403",
        "AY882388",
        "AY882386",
        "AY289094",
        "AY289101",
        "AY882389",
        "AY882390",
        "AF381997",
        "AY195757",
        "AF346975",
        "AF346981",
        "AY882416",
        "Ust_Ishim",
        "BS11",
        "Loschbour",
        "Tianyuan",
        "Kostenki14",
        "Iceman",
        "Eskimo_Saqqaq",
        "Oberkassel998",
        "DolniVestonice14",
        "DolniVestonice13",
        "GoyetQ374a-1",
        "GoyetQ305-7",
        "GoyetQ56-1",
        "Spy_94a",
        "Vindija33.19",
        "Vindija33.16",
        "Vindija33.17",
        "GoyetQ57-3",
        "GoyetQ57-2",
        "Feldhofer1",
        "Vindija33.25",
        "GoyetQ305-4",
        "Feldhofer2",
        "Mezmaiskaya2",
        "ElSidron1253",
        "Chagyrskaya08",
        "Okladnikov2",
        "Les_Cottes_Z4-1514",
        "DC1227",
        "Mezmaiskaya1",
        "Denisova15",
        "Altai",
        "Scladina_I-4A",
        "HST",
        "Denisova4",
        "Denisova3",
        "Denisova8",
        "Denisova2",
        "Sima_de_los_Huesos",
        "Chimpanzee"
    ]

    # overwrite the columns if necessary
    if mode == 'archaics':
        cols = [
            "GoyetQ374a-1",
            "GoyetQ305-7",
            "GoyetQ56-1",
            "Spy_94a",
            "Vindija33.19",
            "Vindija33.16",
            "Vindija33.17",
            "GoyetQ57-3",
            "GoyetQ57-2",
            "Feldhofer1",
            "Vindija33.25",
            "GoyetQ305-4",
            "Feldhofer2",
            "Mezmaiskaya2",
            "ElSidron1253",
            "Chagyrskaya08",
            "Okladnikov2",
            "Les_Cottes_Z4-1514",
            "DC1227",
            "Mezmaiskaya1",
            "Denisova15",
            "Altai",
            "Scladina_I-4A",
            "HST",
            "Denisova4",
            "Denisova3",
            "Denisova8",
            "Denisova2",
            "Sima_de_los_Huesos",
            "Chimpanzee"
        ]       

    filtered_kallisto = kallisto[kallisto.target_id.isin(cols)].copy()
    filtered_kallisto.sort_values('sample', inplace=True)

    data = filtered_kallisto.pivot_table(index="target_id", columns="sample", values="est_counts", sort=False)

    data_norm = data / data.max()
       
    data_sorted = data_norm.reindex(index=cols)
    print(int(len(cols)/5), int(len(data_sorted.columns)/5))

    fig, axes = plt.subplot_mosaic("A", figsize=(int(len(cols)/5), 5+int(len(data_sorted.columns)/5))) #have a minimum of 5

    g = sns.heatmap(
        data_sorted.T,
        square=True,
        cbar=False,
        cmap=sns.light_palette("#225096", as_cmap=True),
        ax=axes["A"]
    )

    axes["A"].set_xlabel("")
    axes["A"].set_ylabel("")

    plt.gca().invert_xaxis()
    g.xaxis.tick_top()
    g.xaxis.set_label_position("top")

    plt.setp(g.get_xticklabels(), rotation=90, ha="left")
    plt.savefig(f"Kallisto_plot_{mode}.svg", dpi=300, transparent=True, bbox_inches="tight")

    data_sorted.to_csv(f"final_kallisto_relative_{mode}.tsv", sep='\t')


if __name__ == '__main__':

    file = sys.argv[1]
    mode = 'all'
    try: 
        if sys.argv[2]=='archaics':
            mode='archaics'
    except IndexError:
        pass

    summarize_kallisto(file, mode)
#! /usr/bin/env python3

from pathlib import Path
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt


def summarize_kallisto(tsv, labels, mode):

    kallisto = pd.read_csv(tsv, sep='\t')
    labels = pd.read_csv(labels, sep='\t')

    cols = labels['Name']
    name_to_label = dict(zip(labels['Name'], labels['Label']))
    
    # how to do the ancient??

    filtered_kallisto = kallisto[kallisto.target_id.isin(cols)].copy()
    filtered_kallisto.sort_values('sample', inplace=True)

    data = filtered_kallisto.pivot_table(index="target_id", columns="sample", values="est_counts", sort=False)

    data_norm = data / data.max()
       
    data_sorted = data_norm.reindex(index=cols)

    fig, axes = plt.subplot_mosaic("A", figsize=(int(len(cols)/5), 5+int(len(data_sorted.columns)/5))) #have a minimum of 5

    g = sns.heatmap(
        data_sorted.T,
        square=True,
        cbar=False,
        cmap=sns.light_palette("#225096", as_cmap=True),
        ax=axes["A"]
    )

    # Replace x-axis tick labels with 'Label' values
    g.set_xticklabels([name_to_label[name] for name in data_sorted.index])

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
    labels = sys.argv[2]
    mode = 'all'
    try: 
        if sys.argv[3]=='archaics':
            mode='archaics'
    except IndexError:
        pass

    summarize_kallisto(file, labels, mode)
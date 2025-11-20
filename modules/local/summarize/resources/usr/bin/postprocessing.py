#! /usr/bin/env python3

from pathlib import Path
import pandas as pd
import seaborn as sns
import sys
import matplotlib.pyplot as plt


def add_group_lines(axis, labels_df, ordered_names,
                    species_col="Species", haplo_col="Haplogroup"):
    """
    Draw species (thick) and haplogroup (thin, only inside species that have >1 haplogroup)
    separators exactly between tick-label positions.

    Call AFTER drawing the heatmap, AFTER setting xticklabels, and AFTER invert_xaxis().
    """

    # --- Must have species column to proceed ---
    if species_col not in labels_df.columns:
        return

    # Build label map in the plotting order
    label_map = labels_df.set_index("Name").loc[ordered_names]
    species_series = label_map[species_col]
    has_haplo = haplo_col in labels_df.columns

    # Helper: find integer boundary indices where change occurs (i means boundary between i-1 and i)
    def find_change_indices(series):
        idxs = []
        for i in range(1, len(series)):
            if series.iloc[i] != series.iloc[i - 1]:
                idxs.append(i)
        return idxs

    # Get tick positions (one per column) to compute exact midpoints between adjacent ticks
    xticks = axis.get_xticks()  # array of positions for tick labels

    def index_to_midpos(i):
        """
        Convert a boundary index 'i' (between i-1 and i) to an axis x-position:
        midpoint of tick positions for i-1 and i when possible, otherwise fallback to i-0.5.
        """
        try:
            if len(xticks) == len(ordered_names):
                return (xticks[i - 1] + xticks[i]) / 2.0
        except Exception:
            pass
        # fallback to data coordinate between cells
        return i - 0.5

    # ---- 1) Species separators (thick) ----
    species_change_idx = find_change_indices(species_series)
    for i in species_change_idx:
        xpos = index_to_midpos(i)
        axis.axvline(x=xpos, color="black", linewidth=1.5, clip_on=False, zorder=5)

    # ---- 2) Haplogroup separators INSIDE each species block (thin) ----
    if not has_haplo:
        return

    haplo_series = label_map[haplo_col].reset_index(drop=True)
    species_vals = species_series.reset_index(drop=True)

    # iterate continuous blocks of same species
    start = 0
    n = len(species_vals)
    for i in range(1, n + 1):
        # end of block when species changes or at final index
        if i == n or species_vals.iloc[i] != species_vals.iloc[i - 1]:
            end = i  # block covers indices [start, end-1]
            block_haplos = haplo_series.iloc[start:end]

            # only draw haplogroup separators if this species has >1 haplogroup
            if block_haplos.nunique(dropna=True) > 1:
                # find local haplogroup change indices inside block (absolute indices)
                for j in range(start + 1, end):
                    if haplo_series.iloc[j] != haplo_series.iloc[j - 1]:
                        xpos = index_to_midpos(j)
                        axis.axvline(x=xpos, color="black", linewidth=0.5, clip_on=False, zorder=6)

            start = i


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

    # Call grouplines on your heatmap
    add_group_lines(g, labels, data_sorted.index)

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
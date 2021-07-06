#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

## GTDB rank-abundance profiles of archaea
dfa = pd.read_csv("gtdb_arch_counts.tab", sep="\t", header=None, names=['phylum','count'])
#dfa.plot(x="phylum", y="count", rot=90, title="Rank-abundance profile of archaeal genomes available on GTDB", color='#d55e00')
#plt.tight_layout()
#plt.savefig('test1a.pdf')

fig, ax = plt.subplots(1, figsize=(8,6))
ax.plot(dfa['phylum'], dfa['count'], color='#d55e00')
ax.set_title("Rank-abundance profile of archaeal genomes available on GTDB")
ax.set_xticks(dfa['phylum'][::1])
ax.set_xticklabels(dfa['phylum'][::1], rotation=90)
plt.tight_layout()
plt.savefig('rank_abund_gtdb_arch.pdf')

## GTDB rank-abundance profiles of bacteria

dfb = pd.read_csv("gtdb_bact_counts.tab", sep="\t", header=None, names=['phylum','count'])
#dfb.plot(x="phylum", y="count", rot=90, title="Rank-abundance profile of bacterial genomes available on GTDB", color='#0072b2')
fig, ax = plt.subplots(1, figsize=(8,6))
ax.plot(dfb['phylum'], dfb['count'], color='#0072b2')
ax.set_title("Rank-abundance profile of bacterial genomes available on GTDB")
ax.set_xticks(dfb['phylum'][::3])
ax.set_xticklabels(dfb['phylum'][::3], rotation=90)
plt.tight_layout()
plt.savefig('rank_abund_gtdb_bact.pdf')

## Silva rank-abundance profiles of archaea

sa = pd.read_csv("silva_arch_phyla_counts.tab", sep="\t", header=None, names=['phylum','count'])
#sa.plot(x="phylum", y="count", rot=90, title="Rank-abundance profile of archaeal 16S sequences available on Silva", color='#d55e00')
#plt.tight_layout()
#plt.savefig('test3.pdf')

fig, ax = plt.subplots(1, figsize=(8,6))
ax.plot(sa['phylum'], sa['count'], color='#d55e00')
ax.set_title("Rank-abundance profile of archaeal 16S sequences available on Silva")
ax.set_xticks(sa['phylum'][::1])
ax.set_xticklabels(sa['phylum'][::1], rotation=90)
plt.tight_layout()
plt.savefig('rank_abund_silva_arch.pdf')

## Silva rank-abundance profiles of bacteria

sb = pd.read_csv("silva_bact_phyla_counts.tab", sep="\t", header=None, names=['phylum','count'])
#sb.plot(x="phylum", y="count", rot=90, title="Rank-abundance profile of bacterial 16S sequences available on Silva", color='#0072b2')
#plt.tight_layout()
#plt.savefig('test4.pdf')
fig, ax = plt.subplots(1, figsize=(8,6))
ax.plot(sb['phylum'], sb['count'], color='#0072b2')
ax.set_title("Rank-abundance profile of bacterial 16S sequences available on Silva")
ax.set_xticks(sb['phylum'][::2])
ax.set_xticklabels(sb['phylum'][::2], rotation=90)
plt.tight_layout()
plt.savefig('rank_abund_silva_bact.pdf')

## Silva rank-abundance profiles of eukarya

se = pd.read_csv("silva_euks_phyla_counts.tab", sep="\t", header=None, names=['phylum','count'])
#sb.plot(x="phylum", y="count", rot=90, title="Rank-abundance profile of eukaryotic 16S sequences available on Silva", color='#009e73')
#plt.tight_layout()
#plt.savefig('test5.pdf')

fig, ax = plt.subplots(1, figsize=(8,6))
ax.plot(se['phylum'], se['count'], color='#009e73')
ax.set_title("Rank-abundance profile of plastid/mitochondrial 16S sequences available on Silva")
ax.set_xticks(se['phylum'][::1])
ax.set_xticklabels(se['phylum'][::1], rotation=90)
plt.tight_layout()
plt.savefig('rank_abund_silva_euks.pdf')





## copy files from Silva db
```
cp ~/databases/silva/all_records_headers.txt .
```


## count bact phyla
```
grep Bacteria all_records_headers.txt | awk '{print $2}' | cut -d ';' -f2 | sort | uniq -c | sort -nr -k1 > bact_phyla_counts.txt
awk 'BEGIN{OFS="\t"}{print $2, $1}' reduced_bact_phyla_counts.txt > reduced_bact_phyla_counts.tab
grep Bacteria all_records_headers.txt | awk '{print $2}' | cut -d ';' -f2 | sort > bact_phyla_for_wordcloud.txt
```

## count cyanos
```
grep Cyanobacteria all_records_headers.txt | awk '{print $2}' | cut -d ';' -f4 | sort | uniq -c | sort -nr -k1 | awk 'BEGIN{OFS="\t"}{print $2, $1}' > cyano_counts.tab
```

## count asgards
```
grep Asgard all_records_headers.txt | awk '{print $2}' | cut -d ';' -f 3 | sort | uniq -c | sort -nr -k1 | awk 'BEGIN{OFS="\t"}{print $2, $1}' > asgard_counts.tab
```

## count archaea
```
grep Archaea all_records_headers.txt | awk '{print $2}' | cut -d ';' -f2 | sort > arch_phyla_for_wordcloud.txt
```

## count eukaryota
```
grep Eukaryota all_records_headers.txt | awk '{print $2}' | cut -d ';' -f2 | sort > euks_phyla_for_wordcloud.txt
```

## make wordclouds
```
Rscript js_make_wordcloud.R -t bact_phyla_for_wordcloud.txt -o bact_phyla_wordcloud.pdf
Rscript js_make_wordcloud.R -t arch_phyla_for_wordcloud.txt -o arch_phyla_wordcloud.pdf
Rscript js_make_wordcloud.R -t euks_phyla_for_wordcloud.txt -o euks_phyla_wordcloud.pdf
```

## copy files over from GTDB
```
cp ~/databases/gtdb/latest_061421/*.tsv .

awk 'BEGIN{FS="\t"}{print $2}' bac120_taxonomy.tsv | cut -d ';' -f 2 | sed 's/p__//g' | sort | uniq -c | sort -nr -k1 | awk 'BEGIN{OFS="\t"}{print $2, $1}' > gtdb_bact_counts.tab
awk 'BEGIN{FS="\t"}{print $2}' bac120_taxonomy.tsv | cut -d ';' -f 2 | sort | sed 's/p__//g' > gtdb_bact_4wordcloud.txt
Rscript js_make_wordcloud.R -t gtdb_bact_4wordcloud.txt -o gtdb_bact_4wordcloud.pdf

awk 'BEGIN{FS="\t"}{print $2}' ar122_taxonomy.tsv | cut -d ';' -f 2 | sed 's/p__//g' | sort | uniq -c | sort -nr -k1 | awk 'BEGIN{OFS="\t"}{print $2, $1}' > gtdb_arch_counts.tab
awk 'BEGIN{FS="\t"}{print $2}' ar122_taxonomy.tsv | cut -d ';' -f 2 | sort | sed 's/p__//g' > gtdb_arch_4wordcloud.txt
Rscript js_make_wordcloud.R -t gtdb_arch_4wordcloud.txt -o gtdb_arch_4wordcloud.pdf
```

## rank abundance profiles
```
grep Bacteria all_records_headers.txt | awk '{print $2}' | cut -d ';' -f2 | sort | uniq -c | sort -nr -k1 | awk 'BEGIN{OFS="\t"}{print $2, $1}' > silva_bact_phyla_counts.tab
grep Archaea all_records_headers.txt | awk '{print $2}' | cut -d ';' -f2 | sort | uniq -c | sort -nr -k1 | awk 'BEGIN{OFS="\t"}{print $2, $1}' > silva_arch_phyla_counts.tab
grep Eukaryota all_records_headers.txt | awk '{print $2}' | cut -d ';' -f2 | sort | uniq -c | sort -nr -k1 | awk 'BEGIN{OFS="\t"}{print $2, $1}' > silva_euks_phyla_counts.tab
python js_make_rankabundplots.py
```

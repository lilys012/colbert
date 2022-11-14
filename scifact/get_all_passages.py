import pandas as pd
import sys
from data_loader import GenericDataLoader

corpus = GenericDataLoader().load_corpus()

pid = 0
cdict = [] # pid : cid
with open("collection.tsv", 'w') as w:
    for cid in corpus.keys():
        text = corpus[cid]['title'] + ' ' + corpus[cid]['text']
        w.write("{}\t{}\n".format(pid, text))
        cdict.append(cid)
        pid += 1

print(pid)
with open("corpus_dict.txt", 'w') as w:
    for i in range(len(cdict)):
        w.write("{}\n".format(cdict[i]))

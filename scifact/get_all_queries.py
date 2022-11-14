import pandas as pd
import sys
from data_loader import GenericDataLoader

queries = GenericDataLoader().load_queries()

qid = 0
cdict = [] # qid : cid

with open("queries.dev.small.tsv", 'w') as w:
    for i, cid in enumerate(queries.keys()):
        if i <= 808:
            continue
        text = queries[cid]
        w.write("{}\t{}\n".format(qid, text))
        cdict.append(cid)
        qid += 1

print(qid)
with open("queries_dict.txt", 'w') as w:
    for i in range(len(cdict)):
        w.write("{}\n".format(cdict[i]))

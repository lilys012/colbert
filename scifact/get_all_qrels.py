from typing import Dict, Tuple
from tqdm.autonotebook import tqdm
import json
import os
import logging
import csv

logger = logging.getLogger(__name__)

reader = csv.reader(open('test.tsv', encoding="utf-8"), delimiter="\t", quoting=csv.QUOTE_MINIMAL)
next(reader)

corpus = {} # original : converted
cid = 0
with open("corpus_dict.txt", "r") as c:
    for line in c:
        text = line[:-1]
        corpus[text] = str(cid)
        cid += 1

queries = {} # original : converted
qid = 0
with open("queries_dict.txt", "r") as q:
    for line in q:
        text = line[:-1]
        queries[text] = str(qid)
        qid += 1

with open("qrels.dev.small.tsv", "w") as w:
    for id, row in enumerate(reader):
        query_id, corpus_id, score = queries[row[0]], corpus[row[1]], int(row[2])
        w.write("{}\t{}\t{}\t{}\n".format(query_id, 0, corpus_id, score))

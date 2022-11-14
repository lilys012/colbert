from colbert.infra import Run, RunConfig, ColBERTConfig
from colbert import Indexer
from colbert import Searcher
from colbert.data import Queries

def main():

    with Run().context(RunConfig(nranks=1, experiment="fiqa")):

        config = ColBERTConfig(
            nbits=2,
            root="/home/intern1001/colbert",
        )
        indexer = Indexer(checkpoint="/media/disk1/intern1001/colbert/colbertv2.0", config=config)
        indexer.index(name="fiqa.nbits=2.zero", collection="/media/disk1/intern1001/colbert/data/fiqa/collection.tsv", overwrite=True)

    with Run().context(RunConfig(nranks=1, experiment="fiqa")):

        config = ColBERTConfig(
            root="/home/intern1001/colbert",
        )
        searcher = Searcher(index="fiqa.nbits=2.zero", config=config)
        queries = Queries("/media/disk1/intern1001/colbert/data/fiqa/queries.dev.small.tsv")
        ranking = searcher.search_all(queries, k=100)
        ranking.save("fiqa.nbits=2.zero.ranking.tsv")

if __name__ == '__main__':
    main()

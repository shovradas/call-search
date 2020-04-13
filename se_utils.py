import math


def term_freq(term, doc, normalized=True):
    if normalized is False:
        return doc.count(term)
    return doc.count(term)/len(doc)


def doc_freq(term, docs):
    occurrences = [1 for doc in docs if term in doc]
    return sum(occurrences)


def inverse_doc_freq(term, docs):
    idf = len(docs)/float(1 + doc_freq(term, docs))  # Adding 1 to avoid division-by-zero
    return math.log(idf, 2)


def tf_idf(term, docs):
    scores = []
    idf = inverse_doc_freq(term, docs)
    for doc in docs:
        scores.append(term_freq(term, doc) * idf)
    return scores

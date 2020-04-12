import feedparser
import se_utils
from flask import Response, request, render_template


def index():
    query = ['Energie',
             'Produktion',
             'Fabrik',
             'Fabrikplanung',
             'Resilienz'
             ]

    with open('doc.html', 'r') as fp:
        doc = fp.read()
        print(doc)


    # docs = [
    #     ['Hello', 'Produktion', 'Energie', 'World', 'Energie', 'Energie'],
    #     ['Hello', 'Bye', 'Energie', 'Resilienz', 'Energie'],
    #     ['Fabrik', 'Produktion', 'Energie', 'Resilienz', 'Fabrikplanung']
    # ]

    # for term in vocab:
    #     print(inverse_doc_freq(term, docs))
    #
    # df = pd.DataFrame(columns=vocab)
    # for doc in docs:
    #     row = pd.Series({term: term_freq(term, doc, False) for term in vocab}, name='doc#')
    #     df = df.append(row)
    #
    # print(df)

    # for term in query:
    #     score = se_utils.tf_idf(term, docs)
    #     print(score)

    return render_template('index.html'), 200


def about():
    return render_template('about.html'), 200
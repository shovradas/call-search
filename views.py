import feedparser
import requests
from flask import Response, request, render_template
import se_utils
import os
from html.parser import HTMLParser
from bs4 import BeautifulSoup


class HTMLFilter(HTMLParser):
    text = ""

    def error(self, message):
        print(message)

    def handle_data(self, data):
        self.text += data
        print(data)


def index():

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

    docs = []
    # feed = feedparser.parse("https://www.foerderdatenbank.de/FDB/DE/Service/RSS/Functions/foerderprogram_rssnewsfeed.xml")
    # for i, item in enumerate(feed.entries):
    #     resp = requests.get(item.link)
    #     with open(f'temp_docs/doc{i}.html', 'w', encoding='utf-8') as fp:
    #         fp.write(resp.text)


    # for doc in os.listdir('temp_docs'):
    #     with open(f'temp_docs/{doc}', 'r', encoding='utf-8') as fp:
    #         docs.append(fp.read())


    # with open(f'temp_docs/doc0.html', 'r', encoding='utf-8') as fp:
    #     doc_html = fp.read()
    #     soup = BeautifulSoup(doc_html, features='html.parser', from_encoding='utf-8')
    #     doc_text = soup.find('main').text
    #     doc_tokenized = doc_text.split()
    #     with open(f'temp_docs/doc_cleaned.txt', 'w', encoding='utf-8') as fp:
    #         fp.write(','.join(doc_tokenized))


    view_data = {
        'keywords': 'Energie,Produktion,Fabrik,Fabrikplanung,Resilienz',
        'source_uri': 'https://www.foerderdatenbank.de/FDB/DE/Service/RSS/Functions/foerderprogram_rssnewsfeed.xml'
    }

    return render_template('index.html', view_data=view_data), 200


def index_post():
    source_uri = request.form['sourceUri']
    keywords = request.form['keywords']

    feed = feedparser.parse(source_uri)
    docs = []
    # for doc in os.listdir('temp_docs'):
    #     with open(f'temp_docs/{doc}', 'r', encoding='utf-8') as fp:
    #         doc_html = fp.read()
    #         #############################
    #         soup = BeautifulSoup(doc_html, features='html.parser', from_encoding='utf-8')
    #         doc_text = soup.find('main').text.lower()
    #         doc_tokenized = doc_text.split()
    #         docs.append(doc_tokenized)

    for entry in feed.entries:
        resp = requests.get(entry.link)
        doc_html = resp.text
        ###################################
        soup = BeautifulSoup(doc_html, features='html.parser', from_encoding='utf-8')
        doc_text = soup.find('main').text.lower()
        doc_tokenized = doc_text.split()
        docs.append(doc_tokenized)

    query = keywords.lower().split(',')
    ranks = []
    for term in query:
        scores = se_utils.tf_idf(term, docs)
        ranks.append(scores)

    result = [0]*len(ranks[0])
    for i in ranks:
        for index, j in enumerate(i):
            result[index] = result[index] + j

    result = dict(enumerate(result))
    result = {k: v for k, v in sorted(result.items(), key=lambda item: item[1], reverse=True)}
    print(result)
    print(result.keys())
    #print(feed.entries)

    entries = [feed.entries[i] for i in list(result.keys())[:5] if result[i]>0]

    view_data = {
        'keywords': keywords,
        'source_uri': source_uri,
        'docs': entries
    }

    return render_template('index.html', view_data=view_data), 200


def about():
    return render_template('about.html'), 200
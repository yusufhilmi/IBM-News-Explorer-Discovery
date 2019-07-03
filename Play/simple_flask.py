import requests
import sys
import os
import json
from flask import Flask

from classified import discovery


app = Flask(__name__)



username = discovery.username
password = discovery.password
environment_id = 'system'
collection_id = 'news-en'


@app.route('/<keyword>')
def news_page(keyword):

    try:

        my_query = discovery.query(environment_id,
                                   collection_id,
                                   count=5,
                                   natural_language_query=keyword)

        data = my_query
        printe = data.result["results"][0]["enriched_title"]["entities"][0]["type"]
        print(printe)

        nodes = []
        links = []

        date = data.result['results'][0]['publication_date']
        print(date)

        summary = data.result['results'][1]['text']
        print(summary)

        sentiment = data.result['results'][1]['enriched_text']['sentiment']['document']['score']
        print(sentiment)

        source = data.result['results'][1]['url']
        print(source)

        type = data.result['results'][1]['enriched_text']['entities'][0]['type']
        print(type)

        document_id = data.result['results'][1]['id']
        name = data.result['results'][1]['title']
        category = data.result['results'][1]['enriched_text']['categories'][0]['label']

        nodes.append(
            {'date': date, 'summary': summary, 'sentiment': sentiment, 'source': source, 'type': type, 'label': name,
             'documentID': document_id, 'category': category, 'id': 42, 'level': 1})
        print(nodes[-1])

        # print("1st Print   URL  :",my_query)
        return str(nodes[-1])

    except Exception as e:
        print(e)





port = os.getenv('VCAP_APP_PORT', '8000')

if __name__ == '__main__':
    app.run(host="127.0.0.2" ,port=int(port), debug=True)

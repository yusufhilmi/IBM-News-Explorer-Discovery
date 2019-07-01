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
                                   count=1,
                                   natural_language_query=keyword)

        response = my_query
        printe = response.result["results"][0]["enriched_title"]["entities"][0]["type"]

        # print("1st Print   URL  :",my_query)
        return str(printe)

    except Exception as e:
        print(e)





port = os.getenv('VCAP_APP_PORT', '8000')

if __name__ == '__main__':
    app.run(host="127.0.0.2" ,port=int(port), debug=True)

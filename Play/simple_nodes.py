import requests
import sys
import os
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash, json, jsonify


"""     --------  For Local Access   -------------
SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static", "IBM_composite_query.json")
data = json.load(open(json_url, encoding="mbcs"))      #encoding fixed mbcs is the correct one 
print(str(data))
"""


app = Flask(__name__)



@app.route('/favicon.ico')
def favicon():
    return "malak"

@app.route('/trial', methods=['GET', 'POST'])
def trial():


    return render_template('cloud_2.html')




@app.route('/', methods=['GET', 'POST'])
def index():
    nodes = []
    links = []

    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static", "IBM_composite_query.json")
    data = json.load(open(json_url, encoding="mbcs"))  # encoding fixed mbcs is the correct one
    index_num = len(data['results'][1]['enriched_text']['entities'])



    # index_res = len(data['results'])

    #  index_num = len(request.json['results'][1]['enriched_text']['entities'])

    count = 0
    nodes.insert(0, {'id': 0, 'label': 'NODES', 'level': 1})


    for i in range(index_num):
        if count > 9:
            break
        else:
            # word = request.json['results'][1]['enriched_text']['entities'][i]['text']
            word = data['results'][4]['enriched_text']['entities'][i]

            # if word['type'] == 'Person':
            # print(word)
            nodes.append({'id': count+1, 'label': word['text'], 'level': 1})
            links.append({'source': count + 1, 'target': 0})
            count += 1

    return render_template('cloud.html', nodes=json.dumps(nodes, indent=2), links=json.dumps(links, indent=2))


port = os.getenv('VCAP_APP_PORT', '8000')

if __name__ == '__main__':
    app.run(port=int(port), debug=True)


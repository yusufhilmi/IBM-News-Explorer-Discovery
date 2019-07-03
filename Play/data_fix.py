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

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "static", "IBM_composite_query.json")
data = json.load(open(json_url, encoding="mbcs"))

nodes = []
links = []

date = data['results'][1]['publication_date']
summary = data['results'][1]['text']
sentiment = data['results'][1]['enriched_text']['sentiment']['document']['score']
source = data['results'][1]['url']
type = data['results'][1]['enriched_text']['entities'][0]['type']
document_id = data['results'][1]['id']
name = data['results'][1]['title']
category = data['results'][1]['enriched_text']['categories'][0]['label']

nodes.append({'date': date, 'summary': summary, 'sentiment': sentiment, 'source': source, 'type': type, 'label': name,
              'documentID': document_id, 'category': category, 'id': 42, 'level': 1})
print(nodes)
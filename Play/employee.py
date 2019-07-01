import os
from flask import Flask, request
import json



app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        value = ""
        index_num = len(request.json['results'][1]['enriched_text']['entities'])

        for i  in range(index_num):
            text = request.json['results'][1]['enriched_text']['entities'][i]['text']
            type = request.json['results'][1]['enriched_text']['entities'][i]['type']
            if type == 'Person':
                value = value + "text: " + text + "    type: " + type + "\n"
        return str(value)

    except Exception as e:
        print(e)





port = os.getenv('VCAP_APP_PORT', '8000')

if __name__ == '__main__':
    app.run( debug=True)

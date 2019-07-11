import logging

import azure.functions as func
from textblob import TextBlob
import nltk
import os
import json

nltk.data.path.append(os.path.join(os.path.curdir, 'nltk_data'))


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    try:
        req_body = req.get_json()
    except ValueError:
        pass
    
    text = req_body['text']
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    return func.HttpResponse(json.dumps(polarity), mimetype='application/json')

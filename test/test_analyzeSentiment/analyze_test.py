import logging

import azure.functions as func
import json
from __app__.analyzeSentiment import main

def test_mytest():

    body = {}
    body['text'] = "I'm so happy"
    body_json = json.dumps(body)
    body_bytes = bytearray(body_json, 'utf-8')
    req = func.HttpRequest(
        'put', 'localhost:7071', body=body_bytes
    )

    ret = main(req)
    assert ret.status_code == 200
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fastapi import FastAPI

app = FastAPI()

import base64
import uuid
import datetime
import hashlib
import hmac


def get_hdr_date():
    return datetime.datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S UTC")

@app.get("/generate-mc-token/{APP_KEY}/")
async def generate_auth(uri, access_key, secret_key,APP_KEY):
 
    # Create variables required for request headers
    request_id = str(uuid.uuid4())
    request_date = get_hdr_date()
 
    unsigned_auth_header = '{date}:{req_id}:{uri}:{app_key}'.format(
        date=request_date,
        req_id=request_id,
        uri=uri,
        app_key=APP_KEY
    )
    hmac_sha1 = hmac.new(
        base64.b64decode(secret_key),
        unsigned_auth_header.encode(),
        digestmod=hashlib.sha1).digest()
    sig = base64.encodebytes(hmac_sha1).rstrip()
    authorization = {"mc-token":'MC ' + access_key + ':' + sig.decode(),
                     "uri":uri,
                     "request-id":request_id,
                     "request-date":request_date
                     }

    return authorization 


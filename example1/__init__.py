import logging

import azure.functions as func
import json
from example1.src.error import Errors

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    body = None
    name = req.params.get('name')
    
    try:
        if not name:
            body = req.get_json()
            raise Exception("Not name")

        name = body.get('name')

        if body == None:
            raise Exception("body none")
    



    except Exception as err:
        #e = Errors(500, None, str(err))
        return func.HttpResponse(
            #body=json.dumps({"error":str(err)}),
            body=e.response(),
            status_code=200,
            mimetype='application/json'
        )

    
    return func.HttpResponse(
        "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        status_code=200
    )   
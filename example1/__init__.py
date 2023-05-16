import logging

import azure.functions as func
import json
from src.error import Errors

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

        if body == None:
            raise ValueError()
    
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
    except Exception as err:
        e = Errors(500, None, str(err))
        return func.HttpResponse(
             #body=json.dumps({"error":str(err)}),
             body=e.response(),
             status_code=200,
              mimetype='application/json'
        )
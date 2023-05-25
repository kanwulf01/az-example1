
import json

class Errors():


    def __init__(self, status, data, error):

        self.status = status
        self.data   = data
        self.error  = error

    def response(self):
        res = {
            "OK":self.status,
            "data":self.data,
            "error":self.error
        }
        return json.dumps(res) 
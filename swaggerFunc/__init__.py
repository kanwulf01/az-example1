import azure.functions as func
import json
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    swagger_file_path = './swagger.json'  # Ruta al archivo Swagger
    
    json_swagger = f"{os.getcwd()}\swaggerFunc\swagger.json"
    print("path", json_swagger)
    with open(json_swagger, 'r') as file:
        swagger_content = file.read()
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    return func.HttpResponse(swagger_content, headers=headers)
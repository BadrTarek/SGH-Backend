from .api_response import ApiResponse
from rest_framework import status 



def project_server():
    return "http://127.0.0.1:8000/"



# headers={'Content-Type':'application/json', 'Authorization':'Bearer d070b44498fd12728d1e1cfbc9aa5f195600d21e'}
#         response = requests.get(project_server()+'/greenhouse/get/'+data["greenhouse_id"] , headers = headers)
#         response.json()
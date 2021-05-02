from typing import Dict, ByteString
import json

import gunicorn.http.body

from models import Graph

'''
Sample request:

{
   "beginning":"start",
   "graph":{
      "a":{
         "c":4,
         "d":2
      },
      "b":{
         "a":8,
         "d":7
      },
      "c":{
         "d":6,
         "end":3
      },
      "d":{
         "end":1
      },
      "end":{
         
      },
      "start":{
         "a":5,
         "b":2
      }
   }
}

'''
# ================= FUNCTION VIEWS =====================

def home(method, body=None):
    data = {"None"}
    response_status = (0,0)
    if method == "GET":
        data = json.dumps({'Welcome': 'please send me some data to handle'})
        response_status = ok_200(data)
    elif method == "POST":

        body_str = body.read().decode('utf-8')
        body_dict = json.loads(body_str)

        data = calculate(body_dict)

        response_status = ok_200(data)

    return {
        "data": data,
        "response_status": response_status
    }

def calculate(graph: Dict):
    graph_dict = graph.get('graph')
    graph_start = graph.get('beginning')
    graph = Graph(graph_dict, graph_start)
    result = graph.count_shortest_path()
    return str(result)


# ================= URLS =====================

urls = {
    "/": home
}

# ================ RETURN CODES =================

def ok_200(data):
    return ("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ])

def not_found_404():
    return ("404 Not Found", [])

def not_allowed_405():
    return ("405 Not Allowed", [])

# ================= DATA HANDLING =====================

def get_bytes(resource) -> ByteString:
    return resource.encode("utf-8")

# ================= MAIN APP =====================

def app(environ: Dict, start_response):
    method = environ.get("REQUEST_METHOD")
    path = environ.get("PATH_INFO")
    body = environ.get("wsgi.input")
    func = urls.get(path)
    if func :
        result = func(method, body)
        data = get_bytes(result.get("data"))
        response_status = result.get("response_status")
        start_response(*response_status)
        return iter([data])
    start_response(*not_found_404())
    return iter([])


import json
from typing import Dict, ByteString, AnyStr

from models import Graph

# ================= CONST ==========================

GREETING_MESSAGE = {"Welcome": "please send me some data to handle"}
NO_BODY_MESSAGE = {"Error": "recived request has empty body"}


# ================= FUNCTION VIEWS =====================
def is_valid_body(body: Dict) -> bool:
    if not isinstance(body, Dict):
        return False
    return True


def home(method: AnyStr, body=None) -> Dict:
    data = {"None"}
    response_status = (0, 0)
    if method == "GET":
        data = json.dumps(GREETING_MESSAGE)
        response_status = ok_200(data)
    elif method == "POST" and is_valid_body(body):
        body_str = body.read().decode('utf-8')
        body_dict = json.loads(body_str)
        data = calculate(body_dict)
        response_status = ok_200(data)
    return {
        "data": data,
        "response_status": response_status
    }


def calculate(graph: Dict) -> AnyStr:
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

def ok_200(data: AnyStr) -> tuple:
    return "200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ]


def not_found_404() -> tuple:
    return "404 Not Found", []


def not_allowed_405() -> tuple:
    return "405 Not Allowed", []


# ================= DATA HANDLING =====================

def get_bytes(resource) -> ByteString:
    return resource.encode("utf-8")


# ================= MAIN APP =====================

def app(environ: Dict, start_response) -> iter:

    method = environ.get("REQUEST_METHOD")
    path = environ.get("PATH_INFO")
    body = environ.get("wsgi.input")
    func = urls.get(path)
    if func:
        result = func(method, body)
        data = get_bytes(result.get("data"))
        response_status = result.get("response_status")
        start_response(*response_status)
        return iter([data])
    start_response(*not_found_404())
    return iter([])

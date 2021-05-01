from typing import Dict, ByteString
import json

# ================= FUNCTION VIEWS =====================

def home(method, body=None):
    data = {"None"}
    response_status = (0,0)
    if method == "GET":
        data = json.dumps({'Welcome': 'please send me some data to handle'})
        response_status = ok_200(data)
    elif method == "POST":
        data = json.dumps(calculate(body))
        response_status = ok_200(data)

    return {
        "data": data,
        "response_status": response_status
    }

def calculate(graph: Dict):
    result = {"distance": 45}
    return result


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
        data = get_bytes(func(method, body).get("data"))
        response_status = func(method, body).get("response_status")
        start_response(*response_status)
        return iter([data])
    start_response(*not_found_404())
    return iter([])


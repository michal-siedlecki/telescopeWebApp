from typing import Dict, ByteString
import json

#================= DATA HANDLING =====================

def render_json(data: Dict):
    return json.dumps(data)


def get_bytes(resource) -> ByteString:
    return resource.encode("utf-8")


def get_data(path, urls):
    for k in urls:
        if k == path:
            func = urls[k]()
            return func


#================= FUNCTION VIEWS =====================

def home():
    return render_json({'index': 'page'})

def echo():
    pass



#================= URLS =====================

urls = {
    "/": home
}

#================= MAIN APP =====================

def app(environ: Dict, start_response):

    method = environ.get("REQUEST_METHOD")
    path = environ.get("PATH_INFO")

    if method == "GET":
        data = get_bytes(get_data(path, urls))
    if method == "POST":
        body = environ.get("wsgi.input")
        user_graph = json.load(body)

        data = get_bytes(get_data(path, urls))



    else:
        data = get_bytes(get_data(path, urls))

    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ])

    return iter([data])


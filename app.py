from typing import Dict, ByteString
import json


def render_json(data: Dict):
    return json.dumps(data)


def get_bytes(resource) -> ByteString:
    return resource.encode("utf-8")


def app(environ: Dict, start_response):

    d = {
        "REQUEST_METHOD": environ.get("REQUEST_METHOD"),
        "PATH_INFO": environ.get("PATH_INFO"),
        "QUERY_STRING": environ.get("QUERY_STRING")
    }

    if environ.get("PATH_INFO") == "/":
        data = get_bytes(render_json(d))
    else:
        start_response("404 Not Found", [])
        return iter([get_bytes("404 error, resource not found")])

    start_response("200 OK", [
        ("Content-Type", "application/json"),
        ("Content-Length", str(len(data)))
    ])
    for k, v in environ.items():
        print(str(k) + ": " + str(v))
    return iter([data])


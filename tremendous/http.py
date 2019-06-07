##############################################################################
# Helper module that encapsulates the HTTPS request so that it can be used
# with multiple runtimes. PK Mar. 14
##############################################################################
import os
import json
import pdb

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

__version__ = '2.0.0'

ALLOWED_METHODS = {'delete', 'get', 'patch', 'post', 'put'}


def _requests(url, access_token, method, data):
    import requests

    normalized_method = method.lower()
    if normalized_method in ALLOWED_METHODS:
        response = getattr(requests, normalized_method)(url, data=json.dumps(data), headers={
            'User-Agent': 'Tremendous Python v{}'.format(__version__),
            'Content-type': 'application/json', 'Accept': 'text/plain',
            'authorization': 'Bearer {}'.format(access_token)
        })

        if response.ok:
            return json.loads(response.text)
        else:
            raise ValueError(response.text)

    else:
        raise ValueError(
            'Invalid request method {}'.format(method)
        )


# Google App Engine
def _urlfetch(url, access_token, method, data):
    from google.appengine.api import urlfetch

    method = method.upper()
    qs = urlencode(data)
    if method == 'POST':
        payload = qs
    else:
        payload = None
        url += '?' + qs

    headers = {
        'User-Agent': 'Tremendous Python v{}'.format(__version__),
        'authorization': 'Bearer {}'.format(access_token)
    }

    res = urlfetch.fetch(
        url,
        follow_redirects=True,
        method=method,
        payload=payload,
        headers=headers,
        deadline=60  # seconds
    )

    # Add consistent interface across requests library and urlfetch
    res.ok = res.status_code >= 200 and res.status_code < 300
    res.text = res.content
    return res


def to_request(access_token, base_url):
    # _is_appengine caches one time computation of os.environ.get().
    # Closure means that _is_appengine is not a file scope variable
    _is_appengine = os.environ.get('SERVER_SOFTWARE', '').split('/')[0] in (
        'Development',
        'Google App Engine',
    )

    req = _urlfetch if _is_appengine else _requests

    def inner(method, path, data=None):
        return req(
            "{}/{}".format(base_url, path),
            access_token,
            method,
            dict(data or {})
        )
    return inner


class AuthenticatedRequest(object):
    def __init__(self, access_token, uri="https://testflight.tremendous.com/api/v2/"):
        if not access_token:
            raise Exception("Access token required for Tremendous API")

        self.requester = to_request(access_token, uri)
        self.uri = uri

    def request(self, method, path, data={}):
        return self.requester(method, path, data)

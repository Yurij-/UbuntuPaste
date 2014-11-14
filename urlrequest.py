# -*- coding:utf-8 -*-

import requests

URL_REQUEST = "http://paste.ubuntu.com"
ARGKEYS = ["id_poster",
           "id_syntax",
           "id_content"]

class RequestURL():
    """
    The class to send request url
    and receive response
    """

    def __init__(self, content):
        """
        init function
        param: CONTENT - map from ARGKEYS to content
        """
        self.content = content

       
    def send(self):
        """
        send request to server
        return: request from server
        """
        r = requests.post(URL_REQUEST, data = self.content)

        return r


def test():
    content = {"poster":"hello",
               "syntax":"python",
               "content":"hello"}

    req = RequestURL(content)
    resp = req.send()

    print (resp.url)

    if resp.history:
        for h in resp.history:
            print (h.url)



test()

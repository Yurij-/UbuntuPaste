# -*- coding:utf-8 -*-
# 
# This file defines the RequestURL class,
# which posts data to the server for response
#
# Author: Kevin Hu

import requests

REQUEST_URL = {"ubuntu": "http://paste.ubuntu.com"}

class RequestURL():
    """
    The class to send request url
    and receive response
    """
    def __init__(self, server, content):
        """
        init function
        param: CONTENT - map from ARGKEYS to content
        """
        if (server not in REQUEST_URL.keys()):
            print("No such service " + server)
            return
        self.url = REQUEST_URL[server]
        self.content = content

       
    def send(self):
        """
        send request to server
        return: request object from server
        """
        self.resp = requests.post(self.server, data = self.content)

        return self.resp


def test():
    """
    Testcase for urlrequest class
    """
    content = {"poster":"hello",
               "syntax":"python",
               "content":"import os\n\nos.listdir('.')\n"}

    req = RequestURL(content)
    resp = req.send()

    print (resp.url)

    if resp.history:
        for h in resp.history:
            print (h.url)


if __name__ == "__main__":
    test()

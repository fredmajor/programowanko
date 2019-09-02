#!/usr/bin/env python3

import requests
from time import sleep


class Request:
    def __init__(self):
        self.closure = None

    def get(self, url):
        print('I will dispatch the GET request now.')
        res = requests.get(url)
        # let's block the thread for some more time, to simulate a long-running
        # request.
        sleep(2)
        print('Request finished. Calling the closure.')
        if self.closure:
            self.closure(res)

    def register_closure(self, closure_function):
        self.closure = closure_function

    def _run(self):
        pass


def main():
    def request_closure(request_results):
        print('I am the closure. Received reply:')
        print(request_results.text)

    request = Request()
    request.register_closure(request_closure)
    request.get('https://api.dopespot.io/v1/version')

    # this is a dummy version. Everything happens in a single thread.
    # the line below will be printed only after the `request.get` call finishes.
    print('I am the main function. If you see this, it means the request '
          'has already finished.')


if __name__ == '__main__':
    main()

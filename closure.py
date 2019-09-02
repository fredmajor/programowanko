#!/usr/bin/env python3

import requests
from time import sleep
import threading


def print_t(str):
    print(f'thread_id: {threading.get_ident()}: {str}')


class Request:
    def __init__(self):
        self.closure = None

    def get(self, url):
        t = threading.Thread(target=self._get, args=(url, ))
        t.start()

    def register_closure(self, closure_function):
        self.closure = closure_function

    def _get(self, url):
        print_t('I will dispatch the GET request now.')
        res = requests.get(url)
        # let's block the thread for some more time, to simulate a long-running
        # request.
        sleep(2)
        print_t('Request has finished. Calling the closure.')
        if self.closure:
            self.closure(res)


def main():
    def request_closure(request_results):
        print_t(f'I am the closure. Received reply: {request_results.text}')

    request = Request()
    request.register_closure(request_closure)
    request.get('https://api.dopespot.io/v1/version')

    # this version uses threads. While the background thread is working on the
    # request, this one can do its stuff.
    print_t('I am the main thread. I will do some work now.')
    for i in range(10):
        # do some complicated task...
        print_t('work work work work work....')
        sleep(0.5)
    print_t('The main thread finished its work.')


if __name__ == '__main__':
    main()

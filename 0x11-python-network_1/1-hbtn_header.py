#!/usr/bin/python3
"""
 displays the value of the X-Request-Id
 variable found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    r = request.Request(argv[1])
    with request.urlopen(r) as r:
        print(r.headers.get('X-Request-Id'))

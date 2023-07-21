#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
                code> <file size>
- After every 10 lines and/or a keyboard interruption (CTRL + C), print these
    statistics from the beginning:
Example:
    File size: 5213
    200: 2
    401: 1
    403: 2
    404: 1
    405: 1
    500: 3
"""
import sys
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
size = 0


def printstats():
    """
    Function that print stats about log
    """
    global size

    print('File size: {}'.format(size))
    stcdor = sorted(codes.keys())
    for each in stcdor:
        if codes[each] > 0:
            print('{}: {}'.format(each, codes[each]))


if __name__ == "__main__":
    cnt = 0
    try:
        """ Iter the standar input """
        for data in sys.stdin:
            try:
                fact = data.split(' ')
                """ If there is a status code """
                if fact[-2] in codes:
                    codes[fact[-2]] += 1
                """ If there is a lenght """
                size += int(fact[-1])
            except BaseException:
                pass
            """ Printing control """
            cnt += 1
            if cnt == 10:
                printstats()
                cnt = 0
    except KeyboardInterrupt:
        printstats()
        raise
    else:
        printstats()

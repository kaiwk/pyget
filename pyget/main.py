import requests


def can_ranged_request(url):
    r = requests.get(url, stream=True)
    return r.headers.get('Accept-Ranges') == 'bytes'


def download(url, start, size):
    if can_ranged_request(url):
        headers = {
            'Range': 'bytes=' + str(start) + '-' + str(start+size-1)
        }
        r = requests.get(url, stream=True, headers=headers)
        with open('test', 'a+b') as f:
            for chunk in r.iter_content(chunk_size=128):
                f.write(chunk)


test_url = 'http://speedtest.tokyo.linode.com/100MB-tokyo.bin'
download(test_url, 0, 1024)

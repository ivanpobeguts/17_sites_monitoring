import requests
import argparse
from datetime import datetime, date, timedelta
import os


def load_urls4check(path):
    urls = []
    with open(path, 'r') as urls_file:
        for line in urls_file:
            urls.append(line.strip())
    return urls


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
    except (requests.exceptions.ConnectionError,
            requests.exceptions.ProxyError):
        return False

    return response.ok


def get_domain_expiration_date(url):
    return datetime(2018, 6, 26, 0, 0)


def count_days_before_expiration(expiration_date):
    delta = expiration_date.date() - date.today()
    return delta >= timedelta(days=30)


def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path',
        '-p',
        help='path to file with urls for check',
    )
    args = parser.parse_args()
    if not os.path.isfile(args.path):
        parser.error(
            "File doesn't exist"
        )
    return parser.parse_args()


if __name__ == '__main__':
    args = get_parser_args()
    urls = load_urls4check(args.path)
    print(urls)
    for url in urls:
        print(is_server_respond_with_200(url))
        print(count_days_before_expiration(get_domain_expiration_date(url)))

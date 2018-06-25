import requests
import argparse
from datetime import datetime
import os
from whois import whois
from urllib.parse import urlparse


def load_urls4check(path):
    with open(path, 'r') as urls_file:
        urls = [line.strip() for line in urls_file]
    return urls


def is_server_respond_with_ok(url):
    try:
        response = requests.get(url)
        return response.ok
    except (requests.exceptions.ConnectionError,
            requests.exceptions.MissingSchema,
            requests.exceptions.ProxyError):
        return False


def get_domain(url):
    return urlparse(url).netloc


def get_domain_expiration_date(domain):
    whois_response = whois(domain)
    whois_expiration_date = whois_response.expiration_date
    if not whois_expiration_date:
        return None
    if isinstance(whois_expiration_date, list):
        return whois_expiration_date[0]
    return whois_expiration_date


def is_enough_days_until_expiration(
    expiration_date,
    expiration_days_limit=30
):
    if expiration_date is None:
        return False
    days_before_expiration = expiration_date - datetime.now()
    return days_before_expiration.days > expiration_days_limit


def get_parser_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path',
        help='path to file with urls for check',
    )
    args = parser.parse_args()
    if not os.path.isfile(args.path):
        parser.error(
            "File doesn't exist"
        )
    return parser.parse_args()


def get_url_info(url):
    url_info = {}
    url_info['url'] = url
    url_info['is_ok'] = is_server_respond_with_ok(url)
    url_info['is_expired'] = is_enough_days_until_expiration(
        get_domain_expiration_date(get_domain(url)))
    return url_info


def print_url_info(url_info):
    print('url:', url_info['url'])
    print('Is url ok: ', 'yes' if url_info['is_ok'] else 'no')
    print('Is domain expired: ', 'yes' if url_info['is_expired'] else 'no')
    print('-' * 30)


if __name__ == '__main__':
    args = get_parser_args()
    urls = load_urls4check(args.path)
    for url in urls:
        print_url_info(get_url_info(url))

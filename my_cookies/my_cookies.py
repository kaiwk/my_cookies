"""Retrieve leetcode cookies from Chrome with local keyring"""

import sys

import click
import browser_cookie3


@click.command()
@click.option('-d', '--domain-name', help='The target domain, e.g. xxx.com')
@click.option('-k', '--keys', help='Keys to retrieve from cookies. '
'It should be the comma separated string, e.g. key1,key2,key3. If it '
'is not specified all keys will be retrieved.')
def retrieve_cookies(domain_name, keys):
    "Retrieve cookies from the domain. Print the result to stdout."
    cookiejar = None

    # For compatibility
    if not domain_name:
        domain_name = "leetcode.com"

    cookie_keys = []
    if keys and len(keys) > 0:
        cookie_keys = [k.strip() for k in keys.split(',')]

    cookie_loaders = {
        "Chrome": browser_cookie3.chrome,
        "Chromium": browser_cookie3.chromium,
        "Brave": browser_cookie3.brave,
        "Librewolf": browser_cookie3.librewolf,
        "Firefox": browser_cookie3.firefox,
        "Edge": browser_cookie3.edge,
        "Vivaldi": browser_cookie3.vivaldi,
        "Opera": browser_cookie3.opera,
    }

    for browser_name, loaders in cookie_loaders.items():
        try:
            # Ideally, we may select the latest cookie, but it's hard to
            # determine which one really is.
            cookiejar = loaders(domain_name=domain_name)
            if cookiejar:
                break
        except Exception as e:
            print(f"Get cookie from {browser_name} failed: {e}",
                  file=sys.stderr)

    if not cookiejar or len(cookiejar) == 0:
        print("Get cookie failed, make sure you have Chrome, Chromium, Brave, Librewolf, "
              "Firefox or Edge installed and login in LeetCode with one of them at "
              "least once.")
        return

    retrieve_all_keys = len(cookie_keys) == 0
    for c in cookiejar:
        if retrieve_all_keys or (c.name in cookie_keys):
            print(c.name, c.value)


def main():
    retrieve_cookies()


if __name__ == "__main__":
    main()

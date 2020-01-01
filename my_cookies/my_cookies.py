"""Retrieve leetcode cookies from Chrome with local keyring"""

from pathlib import Path
import sqlite3
import keyring

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

DB_PATH = (
    Path("~/Library/Application Support/Google/Chrome/Default/Cookies")
    .expanduser()
    .absolute()
)


def clean(decrypted):
    """Function to get rid of padding"""
    return decrypted[: -decrypted[-1]].decode("utf8")


def query_chrome_cookies():
    """Get chrome cookies from sqlite3"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    query_result = cursor.execute(
        "select name, encrypted_value from cookies where host_key like '%leetcode.com'"
    )
    cookies = {}
    for name, encrypted in query_result:
        if name in ("LEETCODE_SESSION", "csrftoken"):
            cookies[name] = encrypted

    conn.commit()
    conn.close()
    return cookies


def decrypt_cookies(cookies):
    """Decrypt cookies."""

    # Default values used by both Chrome and Chromium in OSX and Linux
    salt = b"saltysalt"
    init_vec = b" " * 16
    length = 16

    # On Mac, replace MY_PASS with your password from Keychain
    # On Linux, replace MY_PASS with 'peanuts'
    chrome_pass = keyring.get_password("Chrome Safe Storage", "")
    chrome_pass = chrome_pass.encode("utf8")

    # 1003 on Mac, 1 on Linux
    iterations = 1003

    for name, encrypted in cookies.items():
        key = PBKDF2(chrome_pass, salt, length, iterations)
        cipher = AES.new(key, AES.MODE_CBC, IV=init_vec)
        # Trim off the 'v10' that Chrome/ium prepends
        decrypted = cipher.decrypt(encrypted[3:])
        cookies[name] = clean(decrypted)

    return cookies


def main():
    """Print cookies."""
    cookies = decrypt_cookies(query_chrome_cookies())
    for name, value in cookies.items():
        print(name, value)


if __name__ == "__main__":
    main()

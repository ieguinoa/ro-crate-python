import os
from urllib.parse import urlsplit



def inspect_path(path):
    abs_path = os.path.abspath(path)
    exists = os.path.exists(abs_path)
    is_uri = is_file = is_dir = False
    if not exists:
        upr = urlsplit(path)
        drive, tail = os.path.splitdrive(path)
        if upr.scheme and upr.scheme.lower() != drive.rstrip(":").lower():
            is_uri = True
    if not is_uri:
        is_file = os.path.isfile(abs_path)
        is_dir = os.path.isdir(abs_path)

    return is_file, is_dir, is_uri

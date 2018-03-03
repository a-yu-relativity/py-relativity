"""
client.py
---------
Helper methods for performing HTTP calls.
Wrapper around requests module.
"""

import requests
import base64

# declare constants here
DEFAULT_TIMEOUT = 30 # in seconds
CREDS_FILE = "C:\Creds\creds.txt"

def get_creds(filename):
    """
    Read credentials from a file. Format is:
    URL
    USERNAME
    PASSWORD

    Parameters
    ----------
    filename: string
        path to the file with the credentials

    Returns
    -------
    list as [URL, USERNAME, PASSWORD]
    """
    f = open(filename, "r")
    lines = f.readlines()
    if len(lines) != 3:
        raise ValueError("Not a valid credentials file.")
    # strip out newline chars
    content = [x.rstrip() for x in lines]
    return content


def get_url():
    """
    Returns the base URL of the instance
    """
    content = get_creds(CREDS_FILE)
    return content[0]
    


def get_username():
    """
    Returns the username (email)
    """
    return get_creds(CREDS_FILE)[1]


def get_password():
    """
    Returns the password
    """
    return get_creds(CREDS_FILE)[2]


#----------------------------
# Header info
#----------------------------

def gen_auth_header(username, password):
    unencoded = "{0}:{1}".format(username, password)
    encoded = base64.b64encode(bytes(unencoded, "utf-8"))
    header = "Basic {0}".format(encoded)
    return header


def get_basic_auth_header():
    username = get_username()
    password = get_password()   
    return gen_auth_header(username, password)


def get_headers():
    headers = {}
    headers["authorization"] = get_basic_auth_header()
    headers["content-type"] = "application/json"
    headers["x-csrf-header"] = "-"
    return headers



#----------------------------
# HTTP methods
#----------------------------

def handle_response(r, http_method, custom_err):
    """
    Handles the HTTP response and returns the JSON

    Parameters
    ----------
    r: requests module's response
    
    http_method: string
        "GET", "POST", "PUT", etc.

    custom_err: string
        the custom error message if any

    Returns
    -------
    json : dict

    """
    json = {}
    if r.status_code == requests.codes.ok:
        if r.text:
            json = r.json()
        else:
            print("{0} returned empty response.".format(http_method))
    else:
        if custom_err is not None:
            print(custom_err)
        print("Status code: " + str(r.status_code))
        r.raise_for_status()
    return json


def get(url_ext, query_params={}, custom_err=None, timeout=DEFAULT_TIMEOUT):
    """
    Performs a GET on base_url + url_ext
    e.g. https://my-instance.com + /relativity.REST

    Parameters
    ----------
    url_ext: string
        this is the URL endpoint we are hitting
        (without the host name)

    query_params: dict
        specifies any additional query strings and/or replaces default ones

    custom_err: string
        specifies a custom error message

    timeout: int
        max time the request should wait in seconds

    Returns
    -------
    json : a JSON object (as Python dict)
        the response from the request
    """
    url = get_url + url_ext
    json = {}

    # get request headers
    headers = get_headers()

    r = requests.get(url, params=query_params, headers=headers, timeout=timeout)
    return handle_response(r, "GET", custom_err)


def post(url_ext, query_params={}, payload={}, custom_err=None, timeout=DEFAULT_TIMEOUT):
    """
    Performs a POST on the base_url + url_ext

    Parameters
    ----------
    url_ext: string
        this is the URL endpoint we are hitting
        (without the host name)

    query_params: dict
        specifies any additional query strings and/or replaces default ones

    payload: dict
        JSON payload for request

    custom_err: string
        specifies a custom error message

    timeout: int
        max time the request should wait in seconds

    Returns
    -------
    json : a JSON object (as Python dict)
        the response from the request
    """
    url = base_url + url_ext
    headers = get_headers()
    json = {}

    r = requests.post(url, headers=headers, params=query_params, data=payload, timeout=timeout)
    return handle_response(r, "POST", custom_err)
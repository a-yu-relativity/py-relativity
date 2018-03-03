"""
user.py
---------
CRUD operations on users in Relativity
"""
from pprint import pprint
import json
import client

def create(firstname, lastname, email, password):
    url_ext = "/Relativity.REST/Relativity/User"
    payload = {
        "Artifact Type ID": 2,
        "Artifact Type Name": "User",
        "Parent Artifact": {
            "Artifact ID": 62
        },
        "Groups": [{"Artifact ID": 20}],
        "First Name": firstname,
        "Last Name": lastname,
        "Email Address": email,
        "Type": {
            "Artifact ID": 663,
            "Artifact Type ID": 7,
            "Artifact Type Name": "Choice"
        },
        "Item List Page Length": 25,
        "Client": {
            "Artifact ID": 1024001
        },
        "Authentication Data": "",
        "Default Selected File Type": {
            "Artifact ID": 1014420,
            "Artifact Type ID": 7,
            "Artifact Type Name": "Choice"
        },
        "Beta User": True,
        "Change Settings": True,
        "Trusted IPs": "",
        "Relativity Access": True,
        "Advanced Search Public By Default": False,
        "Native Viewer Cache Ahead": True,
        "Change Password": True,
        "Maximum Password Age": 0,
        "Change Password Next Login": False,
        "Send Password To": {
            "Artifact ID": 1015049,
            "Artifact Type ID": 7,
            "Artifact Type Name": "Choice"
        },
        "Password Action": {
            "Artifact ID": 1015048,
            "Artifact Type ID": 7,
            "Artifact Type Name": "Choice"
        },
        "Password": password,
        "Document Skip": {
            "Artifact ID": 1015042,
            "Artifact Type ID": 7,
            "Artifact Type Name": "Choice"
        },
        "Data Focus": 1,
        "Keyboard Shortcuts": True,
        "Enforce Viewer Compatibility": True,
        "Skip Default Preference": {
            "Artifact ID": 1015044,
            "Artifact Type ID": 7,
            "Artifact Type Name": "Choice"
        }
    }

    payload = json.dumps(payload)
    # specify a custom error message
    error = "Failed to create user with email {0}".format(email)
    results = client.post(url_ext, payload=payload, custom_err=error)
    pprint(results)


def main():
    firstname = "Albert"
    lastname = "Einstein"
    email = "a.einstein@relativity.com"
    password = "Pass1234!"

    result = create(firstname, lastname, email, password)
    pprint(result)


if __name__ == "__main__":
    main()
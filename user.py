"""
user.py
---------
CRUD operations on users in Relativity
"""
from pprint import pprint
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
        "Beta User": true,
        "Change Settings": true,
        "Trusted IPs": "",
        "Relativity Access": true,
        "Advanced Search Public By Default": false,
        "Native Viewer Cache Ahead": true,
        "Change Password": true,
        "Maximum Password Age": 0,
        "Change Password Next Login": false,
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
        "Keyboard Shortcuts": true,
        "Enforce Viewer Compatibility": true,
        "Skip Default Preference": {
            "Artifact ID": 1015044,
            "Artifact Type ID": 7,
            "Artifact Type Name": "Choice"
        }
    }

    # specify a custom error message
    error = "Failed to create user with email {0}".format(email)
    results = client.post(url_ext, payload=payload, custom_err=error)
    pprint(results)


def main():
    firstname = "Albert"
    lastname = "Einstein"
    email = "albert.einstein@relativity.com"
    password = "Password12345!"

    create(firstname, lastname, email, password)


if __name__ == "__main__":
    main()
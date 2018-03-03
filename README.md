# py-relativity
A quick POC of a Python REST client calling Relativity endpoints

## How to use
In the [client.py](client.py) source file, specify a path to a text file with the following three lines:

```
instance URL (e.g. http://my-instance.com)
admin email
admin password
```

Also, in [user.py](user.py) under the `main()` method, specify the parameters of the user you want to create:

```Python
def main():
    firstname = "Albert"
    lastname = "Einstein"
    email = "a.einstein@relativity.com"
    password = "Pass1234!"

    result = create(firstname, lastname, email, password)
    pprint(result)
```


Then run `user.py` like so:
```
python user.py
```

Note: there could be errors in the payload specified in `user.py`, but it worked for me with an ad hoc test

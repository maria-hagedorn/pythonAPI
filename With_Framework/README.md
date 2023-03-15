# Python api with FastAPI framework
A simple python api using the FastAPI framework. Operates on a simple json data file.

## What you need
It would be smart to work in a python environment. If you are unaware of how to create an environment, you can look at it [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

You need to install FastAPI, and Uvicorn to run FastAPI. Using pip both can be installed with:
```
$ python -m pip install fastapi uvicorn[standard]
```
Installing Uvicorn with [standard] means that Uvicorn will install with "Cython-based" dependencies and other optinal extras. For more look at [Uvicorn documentation](https://www.uvicorn.org/).

You also need Pydantic for the data base model, too install run this in the terminal:
```
$ pip install pydantic
```

## Getting started
The server runs at http://127.0.0.1:8000 or http://localhost:8000/. To start the server run the script via Uvicorn:
```
$ uvicorn api_fastapi:app --reload
```
By using the reload tag, when updating the aplication the server will reload automatically. 

When the server is running, you can make a GET, POST, PUT, or DELETE request. To stop the server agian press ```ctrl+c```.

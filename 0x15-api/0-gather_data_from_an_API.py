#!/usr/bin/python3
"""
Retrieves an employees data
with his todo list
"""
import requests
from requests.exceptions import HTTPError
from sys import argv
import json


def fetch_employee(id=None):
    emp = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(id))
    emp = dict(emp.json())
    return emp


def fetch_todos(id=None):
    all_todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos/".format(id))
    all_todos = list(all_todos.json())
    
    completed = []
    for t in all_todos:
        if(t["completed"]):
            completed.append(t)

    return all_todos, completed

if __name__ == "__main__":
    emp_name = fetch_employee(argv[1])["name"]
    all_todos, completed = fetch_todos(argv[1])
    
    print("Employee {} is done with tasks({}/{}):"
            .format(emp_name, len(completed), len(all_todos)))

    for t in completed:
        print("\t{}".format(t["title"]))

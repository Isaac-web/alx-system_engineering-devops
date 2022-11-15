#!/usr/bin/python3
"""
Retrieves an employees data
with his todo list
"""
import json
import requests
from requests.exceptions import HTTPError
from sys import argv


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
    emp_name = fetch_employee(argv[1])["username"]
    all_todos, completed = fetch_todos(argv[1])

    with open("{}.csv".format(argv[1]), "w", encoding="utf-8") as cfile:
        for i in all_todos:
            str = "\"{}\", \"{}\", \"{}\", \"{}\""
            .format(argv[1], emp_name, i['completed'], i["title"])
            cfile.write("{}\n".format(str))

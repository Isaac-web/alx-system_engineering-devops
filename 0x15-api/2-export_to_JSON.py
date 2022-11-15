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
    """
    Returns the todos of the employee with
    the give id
    """
    all_todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos/".format(id))
    all_todos = list(all_todos.json())

    completed = []
    for t in all_todos:
        if(t["completed"]):
            completed.append(t)

    return all_todos, completed


def get_emp_dict(id=None):
    """
    Returns a list of the task of the employee
    """

    all_todos, completed = fetch_todos(id)
    emp = fetch_employee(id)
    formatted_tasks = []
    for t in all_todos:
        formatted_tasks.append(
                {"task": t["title"], "completed": t["completed"],
                    "username": emp["username"]})

    return formatted_tasks


if __name__ == "__main__":
    todos = get_emp_dict(argv[1])
    emp_dict = {}
    emp_dict[str(argv[1])] = todos
    with open("{}.json".format(argv[1]), "w") as file:
        json.dump(emp_dict, file)

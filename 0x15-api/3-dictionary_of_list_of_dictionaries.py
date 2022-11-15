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


def get_emp_ids():
    """
    Returns the ids of all the employees
    """
    res = requests.get("https://jsonplaceholder.typicode.com/users")
    res = res.json()
    emps = list(res)
    ids = []
    for e in emps:
        ids.append(e["id"])
    return (ids)


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
                {"username": emp["username"],
                    "task": t["title"], "completed": t["completed"]})

    return formatted_tasks


if __name__ == "__main__":
    emp_dict = {}
    ids = get_emp_ids()
    for i in ids:
        emp_dict[str(i)] = get_emp_dict(i)

    with open("todo_all_employees.json", "w") as file:
        json.dump(emp_dict, file)

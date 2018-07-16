# Python WorkAround

A module for creating human intelligence tasks (e.g. image labeling,
data entry, performing actions on a website) via WorkAround, a modern, ethical
work sourcing provider.

## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a package manager for Python.

```bash
pip install workaround
```

## Getting Started

If you haven't already, get an API key via [api.workaround.online](https://api.workaround.online).

### Create A Client

```python
from workaround import Client, Task

wao = Client(api_key='YOUR_API_KEY')
```

### Get a Quote

```python
# Quotes are free to create
quote = wao.create_quote()

print("cost per task: $", quote.cost_per_task)
# cost per task: $0.10
```

### Create A Task

```python
task1 = Task(external_url="https://survey.cards/s/rs8Zj4")

wao.create_tasks(quote=quote, tasks=[task1])
```

_tip: To upload custom data with a task, provide `meta={...}`_

### Get Task Information

```python
tasks = wao.get_tasks(task_numbers=[1022, 1024])

print("status:", tasks[0].status)
# status: complete

print("content:", tasks[0].content)
# content: { "question": "some_answer" }
```

### Cancel a Task

```python
print("status:", tasks[1].status)
# status: incomplete

# if you're cancelling multiple tasks, use wao.cancel_tasks(tasks=[...])
tasks[1].cancel()

print("status:", tasks[1].status)
# status: cancelled
```

### Accept or Reject Tasks

```python
tasks = wao.get_tasks(task_numbers=[1022, 1024])

for task in tasks:
  # review tasks using task.meta + task.content
  task.accept() # or task.reject()
```

_tip: To accept/reject tasks in bulk, use `wao.accept_tasks(tasks=[...])` and `wao.reject_tasks(tasks=[...])`_

### Get Billing Information

```python
billing = wao.get_billing()

print("account credit: ", billing.account_credit)
print("quotes created: ", len(billing.quotes))
```

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

### Get a Quote, Create Tasks

```python

# Quotes are free to create
quote = wao.create_quote()

print("cost per task: $", quote.cost_per_task)
# cost per task: $0.10

task1 = Task(external_url="https://survey.cards/s/rs8Zj4")

wao.create_tasks(quote=quote, tasks=[task1])
```





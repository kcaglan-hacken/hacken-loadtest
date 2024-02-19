# Hacken loadtest

## How to run

```python
$ cd /path/to/hacken-loadtest/projects/example-project
$ locust


(env) ╭─kaancaglan@kaancaglan ~/hacken_loadtest/hacken-loadtest/projects/example-project ‹main●› 
╰─$ locust            
'[2024-02-19 15:40:48,423] kaancaglan/WARNING/locust.main: Python 3.8 support is deprecated and will be removed soon
[2024-02-19 15:40:48,424] kaancaglan/INFO/locust.main: Starting web interface at http://0.0.0.0:8089
[2024-02-19 15:40:48,429] kaancaglan/INFO/locust.main: Starting Locust 0.1.dev4588
```

## How To Setup

```python
$ git clone https://github.com/kcaglan-hacken/locust-fork.git
$ git clone https://github.com/kcaglan-hacken/hacken-loadtest.git
$ cd /path/to/hacken-loadtest
$ pip install -r requirements.txt
$ pip install -e /path/to/locust-fork
```
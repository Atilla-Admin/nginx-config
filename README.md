Overview
---

This project aims to ease the configuration of a new virtualhost on a Nginx
frontend.

What does it do ?
---

By taking differents settings from a configuration file or directly from
command line, this script generates a new Nginx virtual host file and adds it
to the current webserver.

Installation
---
This project is using Python 3. Before diving into the project, make sure to
have the following packages installed on your system :

- `python3`
- `python-pip`
- `virtualenv`

Clone the project and set-up the Python environment :

- `git clone <repo url>`
- `virtualenv venv`
- `source venv/bin/activate`
- `pip install -r requirements.txt`

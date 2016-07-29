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

Configuration
---
Most of the configuration parameters can be passed through the command line
arguments, if you want to rely on a stored configuration, edit the
`settings.ini` file.

### Introduce `server-name` and `proxy-pass` variables in your configuration

When writing options in your configuration file, you can choose to use the
`server-name` and the `proxy-pass` variables passed as arguments to the
program.

To archieve this substitution, you can refer to the `server-name` with
`$server-name` and to `proxy-pass` with `$proxy-pass`

#### Example

A configuration defined with :

```
log_path = /var/log/nginx/$server_name
```

… and used with the command :

```python nginx-config.py foo.domain.org foo-prod.domain.org```

… will produce the following log statement in the vhost
file :

```
access_log /var/log/nginx/foo.domain.org/access.log;
```

# heroku-syslog-parser

This utility can be used to parse syslogs sent over HTTPS from Heroku ([see log drains](https://devcenter.heroku.com/articles/log-drains)). You'll need to parse out the bytes per log line ahead of time, since Heroku can batch logs together in a single POST request to your log endpoint.

## usage

```python
from heroku_syslog_parser import HerokuLogParser, ParseError

log_line='<40>1 2017-05-10T06:45:29+00:00 host app web.3 - State changed from starting to up'

try:
    log_dict = HerokuLogParser.parse(log_line)
except ParseError:
    # handle error

print(log_dict['pri'])        # 40
print(log_dict['version'])    # 1
print(log_dict['timestamp'])  # 2017-05-10T06:45:29+00:00
print(log_dict['hostname'])   # host
print(log_dict['appname'])    # app
print(log_dict['procname'])   # web.3
print(log_dict['msg'])        # State changed from starting to up
```

`msg` can be parsed further with the [logfmt package](https://pypi.python.org/pypi/logfmt/0.1)

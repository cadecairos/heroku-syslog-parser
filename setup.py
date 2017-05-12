from distutils.core import setup
setup(
  name = 'heroku-syslog-parser',
  packages = ['heroku_syslog_parser'],
  version = '0.0.4',
  description = 'A tool for parsing rfc5424 formatted syslog messages from Heroku',
  author = 'Chris De Cairos',
  author_email = 'chris@chrisdecairos.ca',
  url = 'https://github.com/cadecairos/heroku-syslog-parser',
  download_url = 'https://github.com/cadecairos/heroku-syslog-parser/archive/0.0.4.tar.gz',
  keywords = ['heroku', 'syslog', 'parser', 'rfc5424'],
  classifiers = [],
)
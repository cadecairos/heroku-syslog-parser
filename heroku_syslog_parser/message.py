import pyparsing

from . import parser

class ParseError(Exception):
    def __init__(self, description, msg):
        self.description = description
        self.msg = msg

    def __repr__(self):
        return '{0}({1!r}, {2!r})'.format(self.__class__.__name__, self.description, self.msg)

    def __str__(self):
        return '{0}: {1!r}'.format(self.description, self.msg)


class HerokuLogParser(object):
    """Representation of a Heroku LogPlex formatted message (after leading byte count removed)"""

    __slots__ = [
        'pri',
        'version',
        'timestamp',
        'hostname',
        'appname',
        'procname',
        'msg',
    ]

    @classmethod
    def parse(self, log_string):
        try:
            groups = parser.heroku_syslog_message.parseString(log_string)
        except pyparsing.ParseException:
            raise ParseError('unable to parse message', log_string)

        return dict(
            (k, getattr(groups, k))
            for k in self.__slots__
        )

    @classmethod
    def parse_dict(self, dict_string):
        try:
            return parser.parse_dict.parseString(dict_string).asDict()
        except pyparsing.ParseException:
            raise ParseError('unable to parse to dict', log_string)

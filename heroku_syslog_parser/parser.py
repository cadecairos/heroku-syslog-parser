from pyparsing import (
    Combine,
    Suppress,
    Word,
    Literal,
    White,
    Optional,
    dictOf,
    alphanums,
    nums,
    printables,
    restOfLine,
    lineEnd,
)

# some constants
SPACE = Suppress(White(ws=' ', min=1, max=1))
DASH = Literal('-')
PLUS = Literal('+')
COLON = Literal(':')
LESS_THAN = Literal('<')
GREATER_THAN = Literal('>')
PERIOD = Literal('.')
TEE = Literal('T')
UNDERSCORE = Literal('_')

# convert values to integers
def toInt(s, loc, toks):
    return int(toks[0])


# pri - '<40>'
pri = Combine(
    Suppress(LESS_THAN)
    + Word(nums, min=1, max=3)
    + Suppress(GREATER_THAN)
).setParseAction(toInt)

# version - '1'
version = Word(nums)
version.setParseAction(toInt)

# date string - 2017-05-10
date = (Word(nums, min=4, max=4)  # year
        + DASH
        + Word(nums, min=2, max=2)  # month
        + DASH
        + Word(nums, min=2, max=2))  # day

# time string - 06:35:24.432+00:00
time = (Word(nums, min=2, max=2)  # hours
        + COLON
        + Word(nums, min=2, max=2)  # minutes
        + COLON
        + Word(nums, min=2, max=2)  # seconds
        + Optional(PERIOD + Word(nums, min=1, max=6))  # milliseconds
        + (DASH | PLUS)
        + Word(nums, min=2, max=2)  # hours offset
        + COLON
        + Word(nums, min=2, max=2))  # minutes offset

# timestamp - 2017-05-10T06:45:29+00:00
timestamp = Combine(date + TEE + time)  # full timestamp

# hostname - host
hostname = Word(printables, min=1, max=255)

# appname - app
appname = Word(printables, min=1, max=255)

# procname - web.1
procname = Word(printables, min=1, max=255)

# msg - State changed from starting to up
msg = restOfLine

heroku_syslog_message = (pri.setResultsName('pri')
                         + version.setResultsName('version')
                         + SPACE + timestamp.setResultsName('timestamp')
                         + SPACE + hostname.setResultsName('hostname')
                         + SPACE + appname.setResultsName('appname')
                         + SPACE + procname.setResultsName('procname')
                         + SPACE + DASH + SPACE
                         + msg.setResultsName('msg')
                         + lineEnd)

# Parse "key=value key=value key="value" key='value'" into a dict
ignore_quotes = Optional(Suppress(Word('"\'')))
label_word = Word(alphanums)
attr_label = Combine(
    label_word,
    UNDERSCORE,
    label_word
)
attr_value = Combine(
    Suppress('=')
    + ignore_quotes
    + Word(printables)
    + ignore_quotes
)

parse_dict = dictOf(attr_label, attr_value)

__all__ = ['heroku_syslog_message', 'parse_dict']

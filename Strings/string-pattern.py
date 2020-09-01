import re

match = re.match('Hello[ \t]*(.*)World', 'Hello     Python World')
print(match.groups())

import yaml
from voluptuous import Schema, Required, Any, Match

schema = Schema({
  Required("name"): str,
  Required("defaults"): {
    Required("sets"): Any(int, Match(r'^(\d+(, \d+)*)$')),
    Required("incr"): str,
    Required("unit"): Any("kgs", "lbs")
  }
}, extra=True)

program = yaml.load(open('program-marcus-5x5.yaml', 'r'))

print schema(program)
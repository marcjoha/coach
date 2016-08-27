import yaml
from voluptuous import Schema, Required, Any, Match, Optional

ValidSets = Any(int, Match(r'^(\d+(, \d+)*)$'))
ValidUnit = Any("kgs", "lbs", "seconds")

schema = Schema({
  Required("name"): str,
  Required("defaults"): {
    Required("sets"): ValidSets,
    Required("incr"): str,
    Required("unit"): ValidUnit
  },
  Required("routine"): [{
    Required("name"): str,
    Required("exercises"): [{
      Required("name"): str,
      Optional("sets"): ValidSets,
      Optional("incr"): str,
      Optional("unit"): ValidUnit
    }]
  }]
})

program = yaml.load(open('program-marcus-5x5.yaml', 'r'))

print schema(program)
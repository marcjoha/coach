import yaml
from voluptuous import Schema, Required, Any, Match, Optional

ValidType = Any("lift", "hold")
ValidSets = Any(int, "AMRAP", Match(r'^((\d|AMRAP)+(, (\d|AMRAP)+)*)$'))
ValidUnit = Any("kgs", "lbs")

schema = Schema({
  Required("name"): str,
  Required("defaults"): {
    Required("type"): ValidType,
    Required("sets"): ValidSets,
    Required("rest"): int,
    Required("incr"): Any(int, float),
    Required("unit"): ValidUnit
  },
  Required("routine"): [{
    Required("name"): str,
    Required("exercises"): [{
      Required("name"): str,
      Optional("type"): ValidType,
      Optional("sets"): ValidSets,
      Optional("incr"): Any(int, float),
      Optional("unit"): ValidUnit
    }]
  }]
})

print schema(yaml.load(open('programs/marcus-5x5.yaml', 'r')))
print schema(yaml.load(open('programs/stronglifts-5x5.yaml', 'r')))
print schema(yaml.load(open('programs/phraks-greyskull-lp.yaml', 'r')))


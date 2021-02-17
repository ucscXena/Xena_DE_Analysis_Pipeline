from appyter.fields import Field
from appyter.ext.json import try_json_loads

class UrlHashCategoryMultiChoiceField(Field):
  '''
  Usage:
    """j2
    {{
      UrlHashMultiChoiceField(
        name="category_case", # the name has to be category_case or category_control
        urlhashkey="category" # (str) the key in url hashed object
        label="a",
        description="B"
      )
    }}
    """
  '''
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  @property
  def raw_value(self):
    value = try_json_loads(self.args['value'])
    if value is None:
      return []
    elif type(value) == list:
      return value
    elif type(value) == str:
      return [value]
    else:
      return [self.args['value']]

  @property
  def value(self):
    if type(self.choices) == dict:
      return [self.choices[v] for v in self.raw_value]
    else:
      assert self.constraint(), '%s[%s] (%s) does not satisfy constraints' % (
        self.field, self.args.get('name', ''), self.raw_value
      )
      return self.raw_value
  
  def constraint(self):
    return True
    #return self.raw_value is not None and all(v in self.choices for v in self.raw_value)

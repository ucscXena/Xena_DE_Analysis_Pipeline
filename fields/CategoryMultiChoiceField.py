from appyter.profiles.default.fields.MultiChoiceField import MultiChoiceField

class CategoryMultiChoiceField(MultiChoiceField):
    def constraint(self):
        return True
        #return self.raw_value is not None and all(v in self.choices for v in self.raw_value)

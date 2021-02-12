from appyter.fields import Field

class UrlHashStringField(Field):
    '''
    Usage:
        """j2
        {{
            UrlHashExprFileField(
                name="A",
                label="a"
            )
        }}
        """
    '''
    def constraint(self):
        return True

from appyter.fields import Field

class UrlHashStringField(Field):
    '''
    Usage:
        """j2
        {{
            UrlHashExprFileField(
                name="A",
                urlhashkey="A",
                label="a"
            )
        }}
        """
    '''

    def __init__(self, constraint=r'.*', hint=None, **kwargs):
        super().__init__(
        constraint=constraint,
        hint=hint,
        **kwargs,
    )

    def constraint(self):
        return True

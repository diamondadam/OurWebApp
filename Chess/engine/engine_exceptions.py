class InvalidMove(Exception):
    # InvalidMove Error 
    def __init__(self, reason):
        self.args = reason,
        self.reason = reason

    def __str__(self):
        return '<InvalidMove error %s>' % self.reason
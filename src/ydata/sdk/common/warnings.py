

class DataSourceTypeWarning(UserWarning):
    pass


class OneTimeWarning(UserWarning):
    RAISED = False

    def __init__(self, message):
        OneTimeWarning.RAISED = True


class NewUserWarning(OneTimeWarning):
    pass

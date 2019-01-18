class BaseDevice:
    def turn_on(self):
        raise NotImplementedError

    def turn_off(self):
        raise NotImplementedError

    def get_state(self):
        raise NotImplementedError

    def register(self):
        raise NotImplementedError

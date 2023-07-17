class Visitor:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if (
            isinstance(new_name, str)
            and not hasattr(self, "_name")
            and 1 <= len(new_name) <= 15
        ):
            self._name = new_name
        else:
            raise Exception

    name = property(get_name, set_name)

    def trips(self):
        from classes.trip import Trip
        return [t for t in Trip.all if t.visitor == self]

    def national_parks(self):
        return list({t.national_park for t in self.trips()})

class NationalPark:
    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if isinstance(new_name, str) and not hasattr(self, "_name"):
            self._name = new_name
        else:
            raise Exception

    name = property(get_name, set_name)

    def trips(self):
        from classes.trip import Trip

        return [t for t in Trip.all if t.national_park == self]

    def visitors(self):
        return {t.visitor for t in self.trips()}

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitors_score = {}
        for t in self.trips():
            if t.visitor not in visitors_score:
                visitors_score[t.visitor] = 1
            else:
                visitors_score[t.visitor] += 1
        return max(visitors_score, key=visitors_score.get)

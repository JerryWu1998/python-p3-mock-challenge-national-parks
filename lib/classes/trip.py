
class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        self.add_trip_to_all(self)

    @classmethod
    def add_trip_to_all(cls, trip):
        cls.all.append(trip)

    def get_visitor(self):
        return self._visitor
    
    def set_visitor(self, new_visitor):
        from classes.visitor import Visitor
        if isinstance(new_visitor, Visitor):
            self._visitor = new_visitor
        else:
            raise Exception
        
    visitor = property(get_visitor, set_visitor)

    def get_national_park(self):
        return self._national_park

    def set_national_park(self, new_national_park):
        from classes.national_park import NationalPark
        if isinstance(new_national_park, NationalPark):
            self._national_park = new_national_park
        else:
            raise Exception

    national_park = property(get_national_park, set_national_park)
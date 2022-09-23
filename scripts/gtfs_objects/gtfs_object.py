
class GTFSObject:
    agency = []
    stops = []
    routes = []
    trips = []
    stop_times = []
    calendar = []
    calendar_dates = []
    fare_attributes = []
    fare_rules = []
    shapes = []
    frequencies = []
    transfers = []
    pathways = []
    levels = []
    feed_info = []
    translations = []
    attributions = []

    file_variables = {}


    def set_file_object(self, name, object, variables):
        self.add_file_object(name, object)
        self.set_file_variables(name, variables)


    def add_file_object(self, name, object):
        if hasattr(name):
            temp_list = getattr(self, name)
            temp_list.append(object)


    def set_file_variables(self, name, variables):
        if hasattr(self, name):
            self.file_variables[name] = variables

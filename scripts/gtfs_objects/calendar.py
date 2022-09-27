
class Calendar:
    #required
    uuid = None
    service_id = None
    start_date = None
    end_date = None

    def __init__(self):
        #required
        self.set_availability(days)


    def set_availability(self, days=[0, 0, 0, 0, 0, 0, 0]):
        """
            Set the availability of the service_id with a list
            - 0 means unavailable
            - 1 means available
            list index 0 starts on monday to list index 6 is sunday
        """
        self.monday = days[0]
        self.tuesday = days[1]
        self.wednesday = days[2]
        self.thursday = days[3]
        self.friday = days[4]
        self.saturday = days[5]
        self.sunday = days[6]

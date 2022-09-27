
class FareAttribute:
    #required
    uuid = None
    fare_id = None
    price = 0
    currency_type = None
    payment_method = None
    transfers = None

    #conditionally required or optional
    agency_id = None
    transfer_duration = None

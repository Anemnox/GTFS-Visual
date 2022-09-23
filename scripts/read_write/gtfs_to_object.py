
import gtfs_objects
from zipfile import ZipFile

import traceback

OBJECT_DICT = {
    "agency": gtfs_objects.Agency,
    "attributions": gtfs_objects.Attribution,
    "calendar": gtfs_objects.Calendar,
    "calendar_dates": gtfs_objects.CalendarDate,
    "fare_attributes": gtfs_objects.FareAttribute,
    "fare_rules": gtfs_objects.FareRule,
    "feed_info": gtfs_objects.FeedInfo,
    "frequencies": gtfs_objects.Frequencies,
    "routes": gtfs_objects.Route,
    "shapes": gtfs_objects.Shape,
    "stop_times": gtfs_objects.StopTime,
    "stops": gtfs_objects.Stop,
    "transfers": gtfs_objects.Transfers,
    "translations": gtfs_objects.Translation,
    "trips": gtfs_objects.Trip
}

def read_gtfs_zip(zip_name):
    full_object = gtfs_objects.GTFSObject()

    with ZipFile(zip_name, "r") as my_zip_file:
        for path in my_zip_file.namelist():
            try:
                name = get_clean_file_name(path)
                if name in OBJECT_DICT.keys():
                    with my_zip_file.open(path) as f:
                        text = [
                            line.decode("utf-8").replace('\n', '')
                            for line in f.readlines()
                            ]
                        [object_part, vars] = gtfs_file_to_object_list(name, text)
                        setattr(full_object, name, object_part)                         # Probably modify this section later
                        full_object.set_file_variables(name, vars)
            except Exception as e:
                print(e)

    return full_object


def get_gtfs_object_from_file(file_name):
    name = get_clean_file_name(file_name)

    values = None
    with open(file_name) as f:
        text = [line.replace('\n', '') for line in f.readlines()]

    return gtfs_file_to_object_list(name, text)



def gtfs_file_to_object_list(name, text):
    """
        Takes in a gtfs file by name and array of text
        by line from the file.
    """
    variables = text[0].split(",")
    object_list = []
    for i in range(1, len(text)):
        values = text[i].split(",")
        data_pack = pack_data(variables, values)
        object_list.append(generate_object(name, data_pack))

    return [object_list, variables]


def pack_data(variable_keys, values):
    if len(variable_keys) != len(values):
        print(variable_keys)
        print(values)
        raise Exception("illegal argument: array size does not match")
    object_pack = {}
    for i in range(len(variable_keys)):
        object_pack[variable_keys[i]] = values[i]

    return object_pack


def generate_object(name, data):
    object = OBJECT_DICT[name]()
    for key in data:
        setattr(object, key, data[key])

    return object


def get_clean_file_name(file_name):
    slash_split = file_name.split("/")
    period_split = slash_split[-1].split(".")
    return list(filter(lambda x: bool(x), period_split))[0]

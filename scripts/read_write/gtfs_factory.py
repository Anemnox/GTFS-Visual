import uuid
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
                        gtfs_file = build_gtfs_file(name, text)
                        setattr(full_object, name, gtfs_file)                         # Probably modify this section later
            except Exception as e:
                print(e)

    return full_object


def load_gtfs_file(file_name):
    name = get_clean_file_name(file_name)

    values = None
    with open(file_name) as f:
        text = [line.replace('\n', '') for line in f.readlines()]

    return build_gtfs_file(name, text)


def build_gtfs_file(name, text):
    """
        Takes in a gtfs file by name and array of text
        by line from the file.
    """
    gtfs_file = gtfs_objects.GTFSFile()
    gtfs_file.name = name
    gtfs_file.variables = text[0].split(",")
    gtfs_file.data = []
    for i in range(1, len(text)):
        try:
            values = text[i].split(",")
            data_pack = pack_data(gtfs_file.variables, values)
            gtfs_file.data.append(build_object(name, data_pack))
        except Exception as e:
            print(e)

    return gtfs_file


def pack_data(keys, values):
    """
        Similar to the zip function. Takes a list of keys
        and list of values to build a dictionary based on
        the order of key and values
    """
    if len(keys) != len(values):
        raise Exception("illegal argument: array size does not match")
    object_pack = {}
    for i in range(len(keys)):
        object_pack[keys[i]] = values[i]

    return object_pack


def build_object(name, data):
    object = OBJECT_DICT[name]()
    object.uuid = str(uuid.uuid4())
    for key in data:
        setattr(object, key, data[key])

    return object


def get_clean_file_name(file_name):
    slash_split = file_name.split("/")
    period_split = slash_split[-1].split(".")
    return list(filter(lambda x: bool(x), period_split))[0]

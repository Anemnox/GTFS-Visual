def parse_gtfs_object(object):
    object_dict = object.__dict__

    gtfs_strings = {}
    for key in object.file_variables:
        variable_keys = object.file_variables[key]
        object_list = object_dict[key]
        gtfs_strings[key] = parse_list_of_gtfs_objects(variable_keys, object_list)

    return gtfs_strings


def parse_list_of_gtfs_objects(variable_keys, object_list):
    texts = [",".join(variable_keys) + '\n']
    for obj in object_list:
        texts.append("".join([parse_gtfs_single_object(obj, variable_keys),"\n"]))
    return texts


def parse_gtfs_single_object(object, variables):
    object_dict = object.__dict__

    text = ""
    for name in variables:
        if name not in object_dict or object_dict[name] is None:
            text = "".join([text, ","])
        else:
            text = "".join([text, str(object_dict[name]), ","])
    text = text[:-1]
    return text

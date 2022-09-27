def parse_gtfs_object(object):
    object_dict = object.__dict__

    gtfs_strings = {}
    for key in object_dict:
        gtfs_file = object_dict[key]
        gtfs_strings[key] = parse_gtfs_file(gtfs_file)

    return gtfs_strings


def parse_gtfs_file(gtfs_file):
    texts = [",".join(gtfs_file.variables) + '\n']
    for obj in gtfs_file.data:
        texts.append("".join([parse_gtfs_single_object(obj, gtfs_file.variables),"\n"]))
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

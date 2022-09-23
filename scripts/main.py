import read_write

def main():
    [agencies, agency_vars] = read_write.get_gtfs_object_from_file("./test_read/agency.txt")
    [stops, stops_vars] = read_write.get_gtfs_object_from_file("./test_read/stops.txt")

    #print(agencies[0].__dict__)

    #for s in stops:
    #    print(s.__dict__)

    #print(read_write.parse_list_of_gtfs_objects(stops_vars, stops))

    stops_text = read_write.parse_list_of_gtfs_objects(stops_vars, stops)
    agency_text = read_write.parse_list_of_gtfs_objects(agency_vars, agencies)

    #read_write.write_to_file("./test_write/stops.txt", stops_text)
    #read_write.write_to_file("./test_write/agency.txt", agency_text)

    obj = read_write.read_gtfs_zip("test_read.zip")

    obj_dat = read_write.parse_gtfs_object(obj)

    read_write.write_all_files("test_output", obj_dat)


if __name__ == '__main__':
    main()

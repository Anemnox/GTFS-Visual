import read_write
import server


def test_server():
    app = server.create_app()

    print('Starting Server')
    app.run(host="0.0.0.0", debug=True)


def main():
    agency_file = read_write.load_gtfs_file("./test_read/agency.txt")
    stops_file = read_write.load_gtfs_file("./test_read/stops.txt")

    #print(agencies[0].__dict__)

    #print(stops_file.__dict__)
    #for s in stops_file.data:
    #    print(s.__dict__)

    #print(read_write.parse_list_of_gtfs_objects(stops_vars, stops))

    stops_text = read_write.parse_gtfs_file(stops_file)
    agency_text = read_write.parse_gtfs_file(agency_file)

    #read_write.write_to_file("./test_write/stops.txt", stops_text)
    #read_write.write_to_file("./test_write/agency.txt", agency_text)

    obj = read_write.read_gtfs_zip("test_read.zip")

    obj_dat = read_write.parse_gtfs_object(obj)

    read_write.write_all_files("test_output", obj_dat)

if __name__ == '__main__':
    test_server()

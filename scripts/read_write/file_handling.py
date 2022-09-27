def write_all_files(dir, file_dat):
    for key in file_dat:
        write_to_file("/".join([dir, key + ".txt"]), file_dat[key])


def write_to_file(file_name, text):
    with open(file_name, "w") as f:
        for t in text:
            f.write(t)

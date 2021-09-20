def decode_line(record):
    """Displays each field of a record"""
    if record[0] != ":":
        raise Exception("Incorrect start code")
    byte_count = record[1:3]
    adress = record[3:7]
    record_type = record[7:9]
    data = ""
    if record_type == "00": # if record == "01" then the data field is empty 
        data = record[9:9 + 2 * int(byte_count, base=16)]
    checksum = record[-2:] # last byte

    print(f"byte_count {byte_count}, adress {adress}, record_type {record_type}, data {data}, checksum {checksum}")


def is_type_data(record):
    """Returns True if the type is 00"""
    return record[7:9] == "00"


def data_from_record(record):
    """Returns the data from a record"""
    byte_count = record[1:3]
    return record[9:9 + 2 * int(byte_count, base=16)]


def decode_file(file_name, out="out.txt"):
    """Returns data of a hex file in a byte array"""
    with open(file_name, "r") as f:
        with open(out, "w") as f2:
            for record in f:
                byte_count = record[1:3]
                if is_type_data(record):
                    data = record[9:9 + 2 * int(byte_count, base=16)]
                    f2.write(data + "\n")



def main():
    decode_file("firmware_tp3_v2.33.hex")


if __name__ == "__main__":
    main()
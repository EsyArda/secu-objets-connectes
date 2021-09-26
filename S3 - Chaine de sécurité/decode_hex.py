import time

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


def decode_file(file_name, out="out.txt", length=0):
    """Returns data of a hex file in a byte array"""
    with open(file_name, "r") as f:
        with open(out, "w", encoding="utf-8") as f2:
            for record in f:
                byte_count = record[1:3]
                if is_type_data(record):
                    data = record[9:9 + 2 * int(byte_count, base=16)]
                    str_ascii = hex_to_ascii(data, length_min=length)
                    f2.write(str_ascii + "\n")


def hex_to_ascii(data, length_min=0):
    s = ""
    temp_s = ""
    for i in range(0, len(data), 2):
        if data[i:i+2].isprintable():
            temp_s += chr(int(data[i:i+2], 16))
        else:
            if len(temp_s) >= length_min:
                s += temp_s
                temp_s = ""
            temp_s = ""
    if len(temp_s) >= length_min:
        s += temp_s
    return s


def main():
    decode_file("./S3 - Chaine de sécurité/firmware_tp3_v2.33.hex", length=3)


if __name__ == "__main__":
    main()
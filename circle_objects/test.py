def convert_num_string(num):

    num_string = str(num)

    parts = []

    if len(num_string) % 2 != 0:
        num_string += "0"

    parts_num = int(len(num_string) / 2)

    current_num = 0
    for i in range(parts_num):
        part_string = ""
        part_string += num_string[current_num]
        part_string += num_string[current_num + 1]
        parts.append(part_string)

        current_num += 2

    return parts


print(convert_num_string(1234))
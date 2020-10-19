my_file = open(r"data.txt", "w")  # r = raw

if my_file.writable():
    my_file.write("Update\n")

    string = ["Johm\n", "Kate\n"]
    my_file.writelines(string)
else:
    print("Can not write")

my_file.close()

#def file_search(file_output, name):


def main():

    file_output = open("New Game -- ", "r")
    name = "kt"
    for line in file_output:
        name_list = line.split()
        if name_list[0] == name:
            print(name_list)









main()
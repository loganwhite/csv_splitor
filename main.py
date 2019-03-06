
import sys
import getopt


"""
    split single csv file into multiple ones
"""
def split_csv(filename):
    dic = dict()
    with open(filename, 'r') as csvfile:
        for line in csvfile:
            str_list = line.split(',')
            index = str_list[0][1:-1]
            if not dic.get(index):
                dic[index] = list()
            dic[index].append(line)
        csvfile.close()

    for key, value in dic.iteritems():
        with open(key + '.csv', 'a') as out_file:
            for item in value:
                out_file.write("%s" % item)
            out_file.close()


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "filename:", ["filename="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err)  # will print something like "option -a not recognized"
        print "f: filename="
        sys.exit(2)

    for o, value in opts:
        if o in ('-f', "--filename"):
            filename = value
            split_csv(filename)

        else:
            assert False, "unhandled option"




if __name__ == '__main__':
    main()
from log_parser import LogsParser


def main():
    # Use a breakpoint in the code line below to debug your script.
    parser = LogsParser('temp.log')
    parser.sanitize()

    # query(t1, t2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

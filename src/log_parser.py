import datetime
import re

import constants as const


class LogsParser:
    def __init__(self, file_addr):
        self.file_addr = file_addr
        self.write_buffer_dict = {}

    @staticmethod
    def _parse_line(line):
        """
        Parses a single line of the log file to generate a LineProperties object
        :param line: Line of a log file
        :return: LineProperties()
        """
        pattern = re.compile('(.*):(.*)::(.*) (.*) (.*) - (.*)')
        m = re.match(pattern, line)
        pid = m.group(1)
        tid = m.group(2)
        t_name = m.group(3)
        date_ = m.group(4)
        time_ = m.group(5)
        date_time = datetime.datetime.strptime(str.format("{} {}", date_, time_), '%Y-%m-%d %H:%M:%S,%f')
        message = m.group(6)
        return LineProperties(pid, tid, t_name, date_time, message)

    def sanitize(self):
        """
        Pre processing sanitization service
        :return:
        """
        input_file = open(self.file_addr, 'r')
        read_buffer = input_file.read(const.NO_OF_BYTES)
        while len(read_buffer) > 0:
            for line in read_buffer.split('\n'):
                if len(line):
                    line_props = self._parse_line(line)
                    if not self.write_buffer_dict.exists(line_props.thread_id):
                        output_filename = str.format("{}_{}", line_props.thread_id, line_props.timestamp)
                        output_file_addr = const.OUTPUT_DIR + output_filename
                        buffered_writer = create_buffer(output_file_addr)
                        self.write_buffer_dict[line_props.thread_id] = buffered_writer


                    if line_props.message == 'end':
                        self.write_buffer_dict[output_filename]

            read_buffer = input_file.read(const.NO_OF_BYTES)

    def query(self, t1, t2):
        """
        Get threads in time interval t1, t2
        :param t1: start timestamp
        :param t2: end timestamp
        :return: Threads info
        """
        pass


class LineProperties:
    def __init__(self, pid, thread_id, thread_name, timestamp, message):
        self.pid = pid
        self.thread_id = thread_id
        self.thread_name = thread_name
        self.timestamp = timestamp
        self.message = message


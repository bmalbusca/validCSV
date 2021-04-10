# -*- coding: utf-8 -*-
"""

Todo:
        * Add check if is convertible
        * Add check number of columns is rigth all file
        * Multiprocessing

.. _Google Python Style Guide:
   http://google.github.io/styleguide/pyguide.html
.. _Napoleon:
   https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

"""

import csv
from functools import reduce
from io import StringIO


class CSVheader:
    """ CSV object validator
    """
    def __init__(self, validator: dict, default: dict = None, ordered = 0, case = 0):
        self.validator = validator
        self.header_config = (ordered << 1) + case
        self.header_default = {0: self.compare_unordered_str, 1: self.compare_case_unorderer_str,
                               2: self.compare_ordered_str, 3: self.compare_case_ordered_str} if not default else default

    def verify_header(self, inputfile):

        wrapper = StringIO(inputfile.readline().decode('utf-8'))
        header = next(csv.reader(wrapper, delimiter=','))
        inputfile.seek(0, 0)

        try:
            return self.header_default[self.header_config](header, self.validator['header'])

        except KeyError as error:
            print("Validator not well defined", error)
        return False

    def compare_case_ordered_str(self, str1: list, str2: list):
        return reduce(lambda b1, b2: b1 and b2, map(lambda x, y: x.lower() == y.lower(), str1, str2))

    def compare_case_unorderer_str(self, str1: list, str2: list):
        str1.sort()
        str2.sort()
        return reduce(lambda b1, b2: b1 and b2, map(lambda e1, e2: e1.lower() == e2.lower(), str1, str2, True))

    def compare_ordered_str(self, str1: list, str2: list):
        for el, vel in zip(str1, str2):
            if el != vel:
                return False
        return True

    def compare_unordered_str(self, str1: list, str2: list):
        str1.sort()
        str2.sort()
        return reduce(lambda b1, b2: b1 and b2, map(lambda e1, e2: e1 == e2, str1, str2))

    def simple_verify_header(self, inputfile, size = None, restrict: bool = True):

        wrapper = StringIO(inputfile.readline().decode('utf-8'))
        str_header = next(csv.reader(wrapper, delimiter=','))
        inputfile.seek(0, 0)

        str_length = len(str_header)

        try:
            if str_length != size:
                return False
        except NameError:
            pass

        try:
            if restrict and len(self.validator["header"]) > str_length:
                return False
            for elem in self.validator["header"]:
                if elem not in str_header:
                    return False
            return True

        except KeyError as error:
            print("Validator not well defined", error)
        return False

    def simple_verify_optional_header(self, inputfile, size = None, restrict: bool = False, options=[]):

        return any([i in options for i in self.validator["header"]]) and self.simple_verify_header( inputfile, size = size, restrict=restrict)



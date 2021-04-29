import re
from src.math_library.math_library import MathLibrary

class ExpressionParser:
    """Parse string containing numbers and operation characters.
        eg. "2+3.4-5*10/7.01^4"
        Returns array where every item is either a float number of character representing operation.
    """

    def solveString(self, string):
        """!
            String consisting of numbers and operators eg "12*3*(34-20/4)" is calculated and returned as float

            @param string String with numbers and operators.
            @return Float result
        """

        items = self._convert_to_depth(string)  # parse parentheses
        items = self._parse_meaning(items)  # convert to floats
        return float(self._solve(items))

    def _push_parentheses(self, obj, result, depth):
        """!
            Helper function for _convert_to_depth. It appends to result object by defined depth.
            @param obj object which will be appended to result
            @param result depth array
            @param depth integer
        """
        while depth:
            result = result[-1]
            depth -= 1

        result.append(obj)

    def _convert_to_depth(self, s):
        """!
        Convert string to array of string characters by its depth defined by parentheses.
        Result is multi-level depth array.

        eg. "10+(2+3)" will return ["1", "0", "+", ["2", "+", "3"]]

        @param s String which will be converted to multilevel array
        @return multilevel array eg. ["1", "0", "+", ["2", "+", "3"]]
        """
        groups = []
        depth = 0

        try:
            for char in s:
                if char == '(':
                    self._push_parentheses([], groups, depth)
                    depth += 1
                elif char == ')':
                    depth -= 1
                else:
                    self._push_parentheses(char, groups, depth)
        except IndexError:
            raise ValueError('Parentheses mismatch')

        if depth > 0:
            raise ValueError('Parentheses mismatch')
        else:
            return groups

    def _parse_meaning(self, items):
        result = []

        number_str = ""
        state = 0
        for i in range(0, len(items)):
            if isinstance(items[i], list):
                fromChild = self._solve(self._parse_meaning(items[i].copy()))
                number_str = number_str + str(fromChild)
                state = 1

            # finite state machine - TODO: Create image
            elif state == 0:
                if items[i].isnumeric():
                    state = 1
                    number_str = number_str + items[i]
                elif items[i] == '-':
                    state = 2
                    number_str = number_str + '-'
            elif state == 1:
                if items[i].isnumeric() or items[i] == '.':
                    # state stays the same
                    number_str = number_str + items[i]
                elif (not items[i].isnumeric()) and (items[i] != '.'):
                    result.append(self._str_to_float(number_str))  # append number
                    number_str = ""
                    state = 3
                    result.append(items[i])  # append operation

            elif state == 2:
                if items[i].isnumeric():
                    state = 1
                    number_str = number_str + items[i]
                else:
                    number_str = number_str + "-"  # because double - - after each other -> one operation, one for number
            elif state == 3:
                if items[i] == '-':
                    state = 2
                    number_str = number_str + '-'
                elif items[i].isnumeric():
                    state = 1
                    number_str = number_str + items[i]

        if number_str:
            result.append(self._str_to_float(number_str))

        return result

    def _str_to_float(self, string):
        # remove double minuses
        string = re.sub('--', '', string)
        try:
            return float(string)
        except ValueError:
            return 0.0

    def _solve(self, items):
        """
        Solve function takes items from a given list of a math expression
        and executes math library functions according to Arithmetic precedence rules

        :param items: (items from list)
        :return result: (final value)
        """

        library = MathLibrary()  # Initialization of Math library
        item_count = len(items)
        i = 0
        while i < item_count:
            if items[i] == "!":  # Checks for factorial, converts to int value
                items[i] = library.factorial(items[i - 1])
                del items[i - 1]
                item_count -= 1
            i += 1

        item_count = len(items)
        i = 0
        while i < item_count:
            if items[i] == "^" or "√":  # Checks for power and square root
                if items[i] == "^":
                    items[i] = library.powerOf(items[i-1], items[i+1])
                    del items[(i - 1):(i + 2):2]
                    item_count -= 2
                    continue
                if items[i] == "√":
                    items[i] = library.squareroot(items[i-1], items[i+1])
                    del items[(i - 1):(i + 2):2]
                    item_count -= 2
                    continue
            i += 1

        item_count = len(items)
        i = 0
        while i < item_count:
            if items[i] == "*" or "/":  # Checks for multiplication and division
                if items[i] == "*":
                    items[i] = library.multiplication(items[i-1], items[i+1])
                    del items[(i - 1):(i + 2):2]
                    item_count -= 2
                    continue
                if items[i] == "/":
                    items[i] = library.division(items[i-1], items[i+1])
                    del items[(i - 1):(i + 2):2]
                    item_count -= 2
                    continue
            i += 1

        item_count = len(items)
        i = 0
        while i < item_count:
            if items[i] == "+" or "-":  # Checks for plus and minus
                if items[i] == "+":
                    items[i] = library.sum(items[i-1], items[i+1])
                    del items[(i - 1):(i + 2):2]
                    item_count -= 2
                    continue
                if items[i] == "-":
                    items[i] = library.difference(items[i-1], items[i+1])
                    del items[(i - 1):(i + 2):2]
                    item_count -= 2
                    continue
            i += 1

        item_count = len(items)
        i = 0
        while i < item_count:
            if items[i] == "%":  # Checks for percent
                items[i] = library.percent(items[i-1], items[i+1])
                del items[(i - 1):(i + 2):2]
                item_count -= 2
                continue
            i += 1

        item_count = len(items)
        i = 0
        while i < item_count:
            if items[i] == "mod":   # Checks for modulo
                items[i] = library.modulo(items[i-1], items[i+1])
                del items[(i - 1):(i + 2):2]
                item_count -= 2
                continue
            i += 1

        result = items[0]
        return result

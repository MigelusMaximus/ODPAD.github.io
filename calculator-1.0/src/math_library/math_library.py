
class MathLibrary:
    """
    Class which performs all mathematical expression calculations.
    """

    def sum(self, a, b):
        """!
            Sum function takes two values, second value is added to the first value

            @param a: first given value (Addend)
            @param b: second given value (Addend)
            @return : Sum
        """
        return a + b

    def difference(self, a, b):
        """!
            Difference function takes two values, first value is subtracted from the second value

            @param a: first given value (Minuend)
            @param b: second given value (Subtrahend)
            @return : Difference
        """
        return a - b

    def multiplication(self, a, b):
        """!
            Multiplication function takes two values, the first value is multiplied by the second value

            @param a: first given value (Multiplicand)
            @param b: second given value (Multiplier)
            @return : Product
        """
        return a * b

    def division(self, a, b):
        """!
            Division function takes two values, the first value is divided by the second value

            @param a: first given value (Dividend)
            @param b: second given value (Divisor)
            @return : Quotient
        """

        if b == 0:
            return Exception("Zero division error")

        return float(a) / float(b)

    def powerOf(self, a, b):
        """!
            PowerOf function takes two values,
            the first value is multiplied by itself b times given by the second value

            @param a: first given value
            @param b: second given value
            @return : Power
        """

        return a ** b

    def factorial(self, a):
        """!
            Factorial function takes one value,
            the value is then multiplied by all positive integers less or equal to the given value

            @param a: first given value (Integer)
            @return : Product
        """

        if abs(round(a)-a) != 0:    # Float point number check
            return Exception("Invalid input")

        neg = False
        if a < 0:   # Negative number case
            neg = True
            a *= -1

        factorial = 1
        for i in range(1, a+1):
            factorial = factorial * i

        if neg:  # Correction for negative number
            factorial *= -1

        return factorial

    def squareroot(self, a, b):  # mistake in naming this should be n-th root  or root
        """!
            Squareroot function takes two values,
            the second value is multiplied by itself a times given by the inverted first value

            @param a: first given value (Degree)
            @param b: second given value (Radicand)
            @return : Root
        """

        if b < 0:  # Radicand can not be less than zero
            return Exception("Invalid input")

        return b ** (1/a)

    def percent(self, a, b):
        """!
            Percent function takes two values, the first value is the total amount (100%),
            the second value is the number of percent set to calculate

            @param a: first given value (Total)
            @param b: second given value (Percent)
            @return : Result
        """
        return a * b / 100

    def modulo(self, a, b):
        """!
            Modulo function takes two values, the first value is divided by the second value,
            but instead of displaying quotient, remainder of the operation is displayed

            @param a: first given value (Dividend)
            @param b: second given value (Divisor)
            @return : Remainder
        """
        if b == 0:
            return Exception("Zero division error")

        return a % b

    # TODO WIP need to ask marian
    def standart_deviation(self, set_of_num):
        size = len(set_of_num)    # Number of numbers in given set

        sig = 0     # Sum
        for i in set_of_num:
            sig += i
        x_ = sig / size     # Arithmetic mean

        sig = 0
        for i in set_of_num:
            sig += (i**2)
        sig -= (size*(x_**2)) / (size-1)

        return #sqr(sig)

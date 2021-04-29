import unittest

from src.expression_parser import ExpressionParser


class TestExpressionParser(unittest.TestCase):
    def setUp(self):
        self.parser = ExpressionParser()


    def test_parse_parentheses(self):
        string_to_parse = "1.5+3.6"
        self.assertEqual(["1", ".", "5", "+", "3", ".", "6"],
                         self.parser._convert_to_depth(string_to_parse))

        string_to_parse = "1*123+ 36"
        self.assertEqual(["1", "*", "1","2","3", "+", " ", "3", "6"],
                         self.parser._convert_to_depth(string_to_parse))

        string_to_parse = "10*(-2*(12+1))+43"
        self.assertEqual(["1", "0", "*", ["-", "2", "*", ["1", "2", "+", "1"]], "+", "4", "3"],
                         self.parser._convert_to_depth(string_to_parse))

        # from documentation of method
        string_to_parse = "10+(2+3)"
        self.assertEqual(["1", "0", "+", ["2", "+", "3"]],
                         self.parser._convert_to_depth(string_to_parse))

    def test_parse_meaning(self):
        list_to_parse = ["1", "-", "-", "4"]
        self.assertEqual([1.0, "-", -4.0], self.parser._parse_meaning(list_to_parse))

        list_to_parse = ["1", "-", "-", "-", "4"]
        self.assertEqual([1.0, "-", 4.0], self.parser._parse_meaning(list_to_parse))

        list_to_parse = ["5", "*", "-", ["455", "+", "1"]]
        self.assertEqual([5.0, "*", -456], self.parser._parse_meaning(list_to_parse))

        list_to_parse = ["5", "*", "-", "-", ["455", "+", "1"]]
        self.assertEqual([5.0, "*", 456], self.parser._parse_meaning(list_to_parse))

        list_to_parse = ["-", "5", "*", "-", "-", ["455", "+", "1"]]
        self.assertEqual([-5.0, "*", 456], self.parser._parse_meaning(list_to_parse))

        list_to_parse = ["1", "0", "+", ["2", "+", "3"]]
        self.assertEqual([10.0, "+", 5.0], self.parser._parse_meaning(list_to_parse))

        # -10 + (2+3) - - 9.4
        list_to_parse = ["-", "1", "0", "+", ["2", "+", "3"], "-", "-", "9", ".", "4"]
        self.assertEqual([-10.0, "+", 5.0, "-", -9.4], self.parser._parse_meaning(list_to_parse))

        # -10 + (2+3) - - - 9.4
        list_to_parse = ["-", "1", "0", "+", ["2", "*", "3"], "-", "-", "-", "9", ".", "4"]
        self.assertEqual([-10.0, "+", 6.0, "-", 9.4], self.parser._parse_meaning(list_to_parse))

        # 1--(2.7+3)
        list_to_parse = ["1", "-", "-", ["2", ".", "7", "+", "3"]]
        self.assertEqual([1.0, "-", -5.7], self.parser._parse_meaning(list_to_parse))
    


    def test_solve(self):
        list = [4.8, "+", 3.0]
        self.assertEqual(7.8, self.parser._solve(list))

        list = [2.0, "+", 3, "*", 5.0, "^", 3.0]
        self.assertEqual(377, self.parser._solve(list))

        list = [2.0, "^", 3, "√", 5.0, "^", 2.0]
        self.assertEqual(1.4953487812212205, self.parser._solve(list))

        list = [5, "!"]
        self.assertEqual(120, self.parser._solve(list))

        list = [5, "!", "/", 10]
        self.assertEqual(12, self.parser._solve(list))

        list = [50, "+", 50, "%", 125, "-", 25]
        self.assertEqual(100, self.parser._solve(list))

        list = [6, "mod", 3]
        self.assertEqual(0, self.parser._solve(list))

        list = [3, "mod", 2]
        self.assertEqual(1, self.parser._solve(list))

    def test_solve_string(self):
        string = "2*5+40"
        self.assertAlmostEqual(50.0, self.parser.solveString(string))

        string = "1.7*(7-1.5)"
        self.assertAlmostEqual(9.35, self.parser.solveString(string))

        string = "5!"
        self.assertAlmostEqual(120.0, self.parser.solveString(string))

if __name__ == '__main__':
    unittest.main()

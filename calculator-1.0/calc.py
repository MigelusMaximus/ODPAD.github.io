from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import webbrowser
from expression_parser import ExpressionParser
from math_library.math_library import MathLibrary

mathLibrary = MathLibrary()
expression_parser = ExpressionParser()

# Set the app size
Window.size = (525,350)

# .kv design file
Builder.load_file('calc.kv')

class CalculatorGuiLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        """!
            Button pressing function.
        """

        # Variable that contains whatever was in the text box already.
        prior = self.ids.calc_input.text

        # Determine if 0 is here.
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.insert_char_to_input(str(button))

        self.ids.calc_input.focus = True

    def button_release(self):
        """!
            Function which gives focus to input after each button is pressed.
        """
        self.ids.calc_input.focus = True

    def insert_char_to_input(self, char):
        # Get character of cursor
        cursor_pos = self.ids.calc_input.cursor[0]
        # Insert character next to cursor
        self.ids.calc_input.insert_text(char)

    def C(self):
        """!
            Function deletes last character.
        """
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}'[:-1]


    def add(self):
        """!
            Function prints '+' at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('+')

    def sub(self):
        """!
            Function prints '-' at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('-')

    def mul(self):
        """!
            Function prints '*' at the end of line.
        """
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f'{prior}*'
        self.insert_char_to_input('*')

    def div(self):
        """!
            Function prints '/' at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('/')

    def perc(self):
        """!
            Function prints '%' at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('%')

    def period(self):
        """!
            Function prints decimal point at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('.')

    def square2(self):
        """!
            Function prints '^(2)' at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('^(2)')

    def square3(self):
        """!
            Function prints '^(3)' at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('^(3)')

    def squareN(self):
        """!
            Function prints '^()' at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('^()')
        self.ids.calc_input.do_cursor_movement("cursor_left")

    def sqroot2(self):
        """!
            Function prints '√()' at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'√()'
        else:
            self.insert_char_to_input('√()')
        self.ids.calc_input.do_cursor_movement("cursor_left")

    def sqroot3(self):
        """!
            Function prints '(3)√()' at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'(3)√()'
        else:
            self.insert_char_to_input('(3)√()')
        self.ids.calc_input.do_cursor_movement("cursor_left")

    def sqrootN(self):
        """!
            Function prints '()√()' at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'()√()'
        else:
            self.insert_char_to_input('()√()')
        self.ids.calc_input.do_cursor_movement("cursor_left")

    def fact(self):
        """!
            Function prints factorial at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('!')

    def pi(self):
        """!
            Function prints 'π' at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'π'
        else:
            self.insert_char_to_input('π')

    def e(self):
        """!
            Function prints 'e' at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'e'
        else:
            self.insert_char_to_input('e')

    def mod(self):
        """!
            Function prints modulo at the end of line.
        """
        prior = self.ids.calc_input.text
        self.insert_char_to_input('mod')

    def sin(self):
        """!
            Function prints 'sin()' at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'sin()'
        else:
            self.insert_char_to_input('sin()')
        self.ids.calc_input.do_cursor_movement("cursor_left")

    def cos(self):
        """!
            Function prints 'cos()' at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'cos()'
        else:
            self.insert_char_to_input('cos()')
        self.ids.calc_input.do_cursor_movement("cursor_left")

    def left_par(self):
        """!
            Function prints left parenthesis at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'('
        else:
            self.insert_char_to_input('(')

    def right_par(self):
        """!
            Function prints right parenthesis at the end of line.
        """
        prior = self.ids.calc_input.text
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f')'
        else:
            self.insert_char_to_input(')')

    def help(self):
        """!
            Function that opens help page.
        """
        webbrowser.open('http://example.com')

    def equals(self):
        """!
            Function evaluates expression.
        """
        prior = self.ids.calc_input.text

        result = expression_parser.solveString(prior)
        self.ids.calc_input.text = str(result)

class CalculatorGui(App):
    def build(self):
        return CalculatorGuiLayout()

if __name__ == '__main__':
    CalculatorGui().run()

from exceptions import InputError, TokenError
import logging

MOVE_RIGHT       = '>'
MOVE_LEFT        = '<'
INCREMENT        = '+'
DECREMENT        = '-'
OUTPUT           = '.'
REPLACE          = ','
JUMP_IF_ZERO     = '['
JUMP_IF_NOT_ZERO = ']'

TOKENS = [MOVE_RIGHT, MOVE_LEFT, INCREMENT, DECREMENT, \
          OUTPUT, REPLACE, JUMP_IF_ZERO, JUMP_IF_NOT_ZERO]

class Brainfuck:
    def __init__(self, program):
        self.index = 0
        self.tokens = Brainfuck.sanitize(program)
        self.brackets = Brainfuck.brackets(self.tokens)

        self.memory = dict()
        self.memory_pointer = 0

        self.operations = {
            MOVE_RIGHT: self.move_right,
            MOVE_LEFT: self.move_left,
            INCREMENT: self.increment,
            DECREMENT: self.decrement,
            OUTPUT: self.output,
            REPLACE: self.replace,
            JUMP_IF_ZERO: self.jump_if_zero,
            JUMP_IF_NOT_ZERO: self.jump_if_not_zero
        }

    def run(self):
        while self.index < len(self.tokens) and self.index >= 0:
            token = self.tokens[self.index]

            try:
                self.operations[token]()
            except KeyError:
                raise TokenError(token, 'Unknown token')

            self.index += 1

    @staticmethod
    def brackets(tokens) -> dict:
        pairs = {}
        stack = []

        for index, token in enumerate(tokens):
            if token == JUMP_IF_ZERO:
                stack.append(index)
            elif token == JUMP_IF_NOT_ZERO:
                if len(stack) == 0:
                    raise IndexError(f'No matching bracket for index {index}.')
                pairs[index] = stack.pop()
        
        if len(stack) > 0:
            raise IndexError(f'No matching opening bracket for index {index}.')

        return pairs
    
    @staticmethod
    def sanitize(program) -> list:
        result = []

        for token in list(program):
            if token in TOKENS:
                result.append(token)

        return result

    def get(self) -> int:
        return self.memory.get(self.memory_pointer, 0)

    def set(self, value):
        self.memory[self.memory_pointer] = value

    def move_right(self):
        self.memory_pointer += 1
    
    def move_left(self):
        self.memory_pointer -= 1

    def increment(self):
        self.set(self.get() + 1 if self.get() < 255 else 0)

    def decrement(self):
        self.set(self.get() - 1 if self.get() > 0 else 255)

    def output(self):
        print(chr(self.get()), end='')

    def replace(self):
        value = input('> ')

        try:
            value = int(value)
        except ValueError:
            raise InputError(value, 'Invalid user input.')

        self.set(value)

    def jump_if_zero(self):
        if self.get() == 0:
            self.index = self.brackets[self.index]

    def jump_if_not_zero(self):
        if self.get() != 0:
            self.index = self.brackets[self.index]

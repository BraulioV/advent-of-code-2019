class IntCodeMachine():

    def __init__(self, program):
        self.program = program
        self.opcodes = {1: lambda x, y: x + y, 
                    2: lambda x, y: x * y,
                    99: None}

    def compute(self):
        position = 0
        while self.program[position] != 99 and self.program[position] in self.opcodes:
            current_opcode = self.program[position]
            first = self.program[self.program[position + 1]]
            second = self.program[self.program[position + 2]]
            self.program[self.program[position + 3]] = self.opcodes[current_opcode](first, second)
            position += 4

    def run(self):
        self.program[1], self.program[2]  = 12, 2
        self.compute()
        return self.program[0]

with open("../data/input") as f:
    data = list(map(lambda x: int(x), f.read().splitlines()[0].split(',')))

print("Program result: {}".format(IntCodeMachine(data).run()))

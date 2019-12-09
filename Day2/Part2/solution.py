class IntCodeMachine():

    def __init__(self, program):
        self.program = list(program)
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

    def run(self, noun = 12, verb = 2):
        self.program[1], self.program[2]  = noun, verb
        self.compute()
        return self.program[0]

def search_noun_verb(data, target):

    for noun in range(0,100):
        for verb in range(0, 100):
            result = IntCodeMachine(data).run(noun, verb)
            if result == target:
                return "Noun: {}, Verb: {}: , Result: {}".format(noun, verb, 100 * noun + verb)

def search_noun_verb_2(data, target):
    noun, verb = 0, 99

    while noun < 100 and verb >= 0:
        result = IntCodeMachine(data).run(noun, verb)
        if result == target:
            return "Noun: {}, Verb: {}: , Result: {}".format(noun, verb, 100 * noun + verb)
        else:
            if result > target:
                verb -= 1
            elif result < target:
                noun += 1 


with open("../data/input") as f:
    data = list(map(lambda x: int(x), f.read().splitlines()[0].split(',')))

search_noun_verb_2(data, 19690720)
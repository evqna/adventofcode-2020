from tool.runners.python import SubmissionPy

class Interpreter:

    def __init__(self, instructions):
        self.prog = instructions
        self.ip = 0
        self.acc = 0
        self.trace = set()
    
    def step(self):
        op, arg =  self.prog[self.ip]
        if op == 'acc':
            self.acc += int(arg)
        elif op == 'jmp':
            self.ip += int(arg) - 1
        self.ip += 1

    def run(self):
        '''Run until a loop is detected'''
        while self.ip not in self.trace:
            self.trace.add(self.ip)
            self.step()

class EvqnaSubmission(SubmissionPy):

    def run(self, s):
        program = [instr.split() for instr in s.splitlines()]
        pc = Interpreter(program)

        pc.run()
        return pc.acc

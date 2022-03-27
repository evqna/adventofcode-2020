from tool.runners.python import SubmissionPy

class Interpreter:

    def __init__(self, instructions):
        self.prog = instructions
        self.ip = 0
        self.acc = 0
        self.trace = set()
    
    def step(self):
        op, arg = self.prog[self.ip]
        if op == 'acc':
            self.acc += int(arg)
        elif op == 'jmp':
            self.ip += int(arg) - 1
        self.ip += 1

    def run(self):
        '''Run until a loop is detected or the program terminates'''
        while True:
            if self.ip in self.trace:
                return False
            if self.ip >= len(self.prog):
                return True
            self.trace.add(self.ip)
            self.step()
    
    def run_with_branching(self):
        while True:
            op = self.prog[self.ip][0]
            if op == 'nop' or op == 'jmp':
                self.patch_program(self.ip)
                forked_pc = self.fork()
                if forked_pc.run():
                    self.acc = forked_pc.acc
                    self.ip = forked_pc.ip
                    self.trace = forked_pc.trace
                    return
                else:
                    self.patch_program(self.ip)     # Undo patch
            self.trace.add(self.ip)
            self.step()

    def patch_program(self, i):
        self.prog[i][0] = 'jmp' if self.prog[i][0] == 'nop' else 'nop'

    def fork(self):
        forked_pc = Interpreter(self.prog)
        forked_pc.acc = self.acc
        forked_pc.trace = self.trace.copy()
        forked_pc.ip = self.ip
        return forked_pc

class EvqnaSubmission(SubmissionPy):

    def run(self, s):
        program = [instr.split() for instr in s.splitlines()]
        pc = Interpreter(program)

        pc.run_with_branching()
        return pc.acc

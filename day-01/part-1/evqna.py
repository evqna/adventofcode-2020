from tool.runners.python import SubmissionPy


class EvqnaSubmission(SubmissionPy):

    def run(self, s):
        entries = {int(line) for line in s.split()}
        for a in entries:
            b = 2020 - a
            if b in entries:
                return a * b

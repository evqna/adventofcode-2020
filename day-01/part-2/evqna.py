from tool.runners.python import SubmissionPy


class EvqnaSubmission(SubmissionPy):

    def run(self, s):
        entries = {int(line) for line in s.split()}
        for a in entries:
            for b in entries:
                c = 2020 - a - b
                if c in entries:
                    return a * b * c

from tool.runners.python import SubmissionPy


class EvqnaSubmission(SubmissionPy):

    def is_valid(self, password_entry):
        policy, c, pwd = password_entry.split()
        a, b = policy.split('-')
        i, j = int(a) - 1, int(b) - 1
        return (pwd[i] == c[0]) ^ (pwd[j] == c[0])

    def run(self, s):
        return sum(1 for entry in s.splitlines() if self.is_valid(entry))

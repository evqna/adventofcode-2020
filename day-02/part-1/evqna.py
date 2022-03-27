from tool.runners.python import SubmissionPy


class EvqnaSubmission(SubmissionPy):

    def is_valid(self, password_entry):
        policy, c, pwd = password_entry.split()
        policy_min, policy_max = policy.split('-')
        return int(policy_min) <= pwd.count(c[0]) <= int(policy_max)

    def run(self, input):
        return sum(1 for entry in input.splitlines() if self.is_valid(entry))

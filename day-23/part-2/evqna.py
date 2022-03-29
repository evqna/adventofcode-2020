from tool.runners.python import SubmissionPy

CUPS = 10**6
ROUNDS = 10**7

class EvqnaSubmission(SubmissionPy):
    def generate_lookup_table(self, cups):
        # Simulate a linked list by storing next labels into a lookup table
        n = [i + 1 for i in range(CUPS + 1)]
        for i, label in enumerate(cups[:-1]):
            n[label] = cups[i + 1]
        n[cups[-1]] = max(cups) + 1  # Link input to remaining cups
        n[-1] = cups[0]              # Wrap around
        return n
    
    def run(self, s):
        cups = [int(c) for c in s.strip()]
        n = self.generate_lookup_table(cups)

        # Throwing everything into a single loop helps control the run time,
        # otherwise there is a large performance penalty when accessing member fields
        # or functions.
        current = cups[0]
        for _ in range(ROUNDS):
            a = n[current]
            b = n[a]
            c = n[b]

            dest = current - 1
            while dest < 1 or dest in (a, b, c):
                if dest < 1:
                    dest = CUPS
                else:
                    dest -= 1

            tail = n[c]
            n[c] = n[dest]
            n[dest] = a
            n[current] = tail
            # Rotate current cup
            current = n[current]

        return n[1] * n[n[1]]

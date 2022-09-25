from tool.runners.python import SubmissionPy

import math


class EvqnaSubmission(SubmissionPy):
    def discrete_log(self, A, g, n):
        m = int(math.sqrt(n)) + 1
        lookup = {}

        # Baby steps
        g_x = 1
        for i in range(m):
            lookup[g_x] = i
            g_x = (g_x * g) % n

        # Giant steps
        I = pow(g, -m, mod=n)
        for i in range(m):
            if A in lookup:
                return i * m + lookup[A]
            A = (A * I) % n

    def run(self, s):
        g, p = 7, 20201227
        P, Q = [int(c) for c in s.splitlines()]

        d = self.discrete_log(Q, g, p)
        return pow(P, d, mod=p)

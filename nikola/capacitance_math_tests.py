import unittest

import nikola.capacitance_math as cm


class CapMathTests(unittest.TestCase):
    def assertBounded(self, value: float, lower: float, upper: float):
        self.assertLess(lower, upper, "Test Configuration issue")
        self.assertGreater(value, lower)
        self.assertLess(value, upper)

    def test_wrt_deepfried_neon1(self):
        # http://deepfriedneon.com/tesla_f_calctoroid.html
        # The results for 15 inches x 4 inches is 16.648 pF
        self.assertBounded(cm.ToroidEstimators.toroid_estimate_1(4, 15), 15, 26)
        self.assertBounded(cm.ToroidEstimators.toroid_estimate_2(4, 15), 15, 26)
        self.assertBounded(cm.ToroidEstimators.toroid_estimate_3(4, 15), 15, 26)

    def test_wrt_deepfried_neon2(self):
        # http://deepfriedneon.com/tesla_f_calctoroid.html
        # The results for 30 inches x 8 inches is 33.296 pF
        self.assertBounded(cm.ToroidEstimators.toroid_estimate_1(8, 33), 30, 52)
        self.assertBounded(cm.ToroidEstimators.toroid_estimate_2(8, 33), 30, 52)
        self.assertBounded(cm.ToroidEstimators.toroid_estimate_3(8, 33), 30, 52)

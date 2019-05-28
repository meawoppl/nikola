import numpy as np


class ToroidEstimators:
    """
    Based loosely on http://www.teslacoildesign.com/design.html#design_topload
    Similar equations found here:
    http://deepfriedneon.com/tesla_f_calctoroid.html

    Note, these functions assume the shape of:

    d2 {  0--0

          |--|
           d1

    NB: These are full of magic numbers, most notably the numbers which
    are c. 1.27...  seem to have units of pF / inch?

    I _believe_ these are
    """

    MAGIC_1 = 1.2781
    MAGIC_2 = 1.2800
    MAGIC_3 = 1.252296756620

    @staticmethod
    def toroid_estimate_1(d2, d1):
        assert d2 < d1

        ratio = d2 / d1
        prod = d2 * d1

        c1 = (ToroidEstimators.MAGIC_1 - ratio) * np.sqrt(2 * np.pi * prod)

        return c1

    @staticmethod
    def toroid_estimate_2(d2, d1):
        assert d2 < d1

        ratio = d2 / d1
        prod = d2 * d1
        ring_sq = d2 * d2

        c2 = (ToroidEstimators.MAGIC_2 - ratio) * np.sqrt(2 * np.pi * (prod - ring_sq))

        return c2

    @staticmethod
    def toroid_estimate_3(d2, d1):
        assert d2 < d1

        prod = d2 * d1
        ring_sq = d2 * d2

        c3 = ToroidEstimators.MAGIC_3 * np.sqrt(2 * np.pi * (prod - ring_sq))

        return c3

    @staticmethod
    def toroid_estimate_mean(ring_d_inches, overall_d_inches):
        assert ring_d_inches < overall_d_inches

        c1 = ToroidEstimators.toroid_estimate_1(ring_d_inches, overall_d_inches)
        c2 = ToroidEstimators.toroid_estimate_2(ring_d_inches, overall_d_inches)
        c3 = ToroidEstimators.toroid_estimate_3(ring_d_inches, overall_d_inches)

        return (c1 + c2 + c3) / 3.0

# -*- coding: utf-8 -*-

import numpy as np


def bootstrap_CI(data1, data2, num_draws=10000):
    """
    Computes 95% confidence interval for the mean difference between data1 and data2

    Parameters
    ----------
    data1: array_like
        The data you desire to calculate confidence interval for

    data2: array_like
        The data you desire to calculate confidence interval for

    num_draws: int
        Number of draws to be used for the computation of the CI. The default value is set to 10000

    Returns
    -------
    ndarray
        An array containing the 2.5 percentile at index 0 and the 97.5 percentile at index 1
    """
    means = np.zeros(num_draws)
    data1 = np.array(data1)
    data2 = np.array(data2)
    N1 = len(data1)
    N2 = len(data2)

    for n in range(num_draws):
        data1_tmp = np.random.choice(data1, N1)
        data2_tmp = np.random.choice(data2, N2)
        means[n] = np.nanmean(data1_tmp) - np.nanmean(data2_tmp)

    return [np.nanpercentile(means, 2.5), np.nanpercentile(means, 97.5)]

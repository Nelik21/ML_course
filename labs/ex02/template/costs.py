# -*- coding: utf-8 -*-
"""Function used to compute the loss."""

def compute_loss(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    return (y-w-tx).transpose*(y-w-tx)
    raise NotImplementedError

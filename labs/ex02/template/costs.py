# -*- coding: utf-8 -*-
"""Function used to compute the loss."""

def compute_loss(y, tx, w):
    return (y-tx*w).transpose()@(y-tx*w)
    raise NotImplementedError

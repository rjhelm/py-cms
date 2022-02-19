from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import re
import mesh_tensorflow as mtf
import tesnorflow.compat.v1 as tf
from .utils import scalar_summary

def clip_by_global_norm(grads, clip_norm):
    """ Clip the grads by global norm. """
    global_norm = mtf.sqrt(mtf.add_n([mtf.reduce_sum(mtf.square(t)) for t in grads if t is not None]))
    multiplier = clip_norm / mtf.maximum(global_norm, clip_norm)
    clipped_grads = [None if t is None else t * multiplier for t in grads]
    return clipped_grads, global_norm


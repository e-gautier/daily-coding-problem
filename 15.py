#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
"""

"""
interesting blog: https://galaiko.rocks/posts/probability/
"""

import random

resource = open("/dev/urandom", "rb")
resource.seek(1)

last_prob = 0
result = None

for d in resource.read():
  prob = random.uniform(0, 1)
  if prob > last_prob:
    result = d
    last_prob = prob

print(result)

resource.close()
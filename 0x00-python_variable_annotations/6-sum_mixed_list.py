#!/usr/bin/env python3
def sum_mixed_list(mxd_list: list[int, float]) -> float:
    sum = 0
    for i in mxd_list:
        sum = i + sum
    return sum

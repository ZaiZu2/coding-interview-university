from typing import Iterable, Any, Sequence, Callable
import os


########################################################################################
# English Ruler - pg 152
def draw_line(tick_length: int, tick_label: int = "") -> None:
    tick = "-" * tick_length
    if tick_label:
        tick += " " + tick_label
    print(tick)


def draw_interval(center_length: int) -> None:
    if center_length > 0:
        draw_interval(center_length - 1)
        draw_line(center_length)
        draw_interval(center_length - 1)


def draw_ruler(inches: int, major_length: int) -> None:
    draw_line(major_length, "0")
    for i in range(inches):
        draw_interval(major_length - 1)
        draw_line(major_length, str(i + 1))


# draw_ruler(3, 4)


########################################################################################
# Binary search - pg 155
def binary_search(data: Sequence, target: Any, low: int, high: int) -> bool:
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binary_search(data, 3, 0, len(data) - 1))


# Every tail recursive function can be converted to an iterative function
# Binary search iterative - pg 179
def binary_search_iterative(data: Sequence, target: Any) -> bool:
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = high + low // 2

        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binary_search_iterative(data, 23))


########################################################################################
# Disk usage - pg 159
def disk_usage(path: str) -> int:
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)

    print(f"{total:10}   {path}")
    return total


# disk_usage(os.getcwd())


########################################################################################
# Recursive check if sequence is unique- pg 159
def is_unique(S: Iterable, start: int, stop: int) -> bool:
    """Return True if there are no duplicate elements in slice S[start:stop]"""
    if stop - start <= 1:
        return True  # at most one item
    elif not is_unique(S, start, stop - 1):
        return False  # first part has duplicate
    elif not is_unique(S, start + 1, stop):
        return False  # second part has duplicate
    else:
        return S[start] != S[stop - 1]  # do first and last differ?


# print(is_unique([1, 2, 3, 4, 5], 0, 5))


########################################################################################
# Fibonacci - pg 166
def bad_fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return bad_fibonacci(n - 1) + bad_fibonacci(n - 2)


# print(bad_fibonacci(8))


def good_fibonacci(n: int) -> tuple[int, int]:
    if n <= 1:
        return (n, 0)
    else:
        (a, b) = good_fibonacci(n - 1)
        return (a + b, a)


# print(good_fibonacci(8)[0])


########################################################################################
# Reverse a list - pg 171
def reverse_list(S: list, start: int, stop: int) -> None:
    if start + 1 >= stop:
        return

    S[start], S[stop] = S[stop], S[start]
    return reverse_list(S, start + 1, stop - 1)


# a = [1, 2, 3, 4, 5, 6]
# reverse_list(a, 0, 5)
# print(a)


# Every tail recursive function can be converted to an iterative function
def reverse_list_iterative(S: list):
    start = 0
    stop = len(S) - 1
    while start <= stop:
        S[start], S[stop] = S[stop], S[start]
        start += 1
        stop -= 1

a = [1, 2, 3, 4, 5, 6]
reverse_list_iterative(a)
print(a)

########################################################################################
# Power - pg 172


# Time complexity O(n)
def bad_power(x: int, n: int) -> int:
    if n == 0:
        return 1
    return x * bad_power(x, n - 1)


# Time and space complexity O(logn)
def good_power(x: int, n: int) -> int:
    if n == 0:
        return 1

    partial = good_power(x, n // 2)

    if n % 2 != 0:
        return x * partial * partial
    else:
        return partial * partial


# print(good_power(2, 8))


########################################################################################
# Sum sequence elements - pg 174
def binary_sum(S: Iterable, start: int, stop: int) -> int:
    if start >= stop:
        return 0
    elif start == stop - 1:
        return S[start]

    mid = (start + stop) // 2
    return binary_sum(S, start, mid) + binary_sum(S, mid, stop)


# a = [2, 2, 2, 2, 2]
# print(binary_sum(a, 0, 5))


########################################################################################
# TODO: You messed that up completely, redo
# solve a summation puzzle - pg 176
# def solve_puzzle(
#     sequence: Sequence, values: list[int], test_fn: Callable[[Sequence], bool]
# ) -> Sequence | None:
#     for value in values:
#         new_sequence = sequence + [value]
#         new_values = values.copy()
#         new_values.remove(value)
#         if len(new_values) == 0:
#             if test_fn(new_sequence):
#                 print(f'Conforming sequence: {"".join([str(s) for s in new_sequence])}')
#                 return new_sequence
#         else:
#             print(f'Trying sequence: {"".join([str(s) for s in new_sequence])}')
#             solve_puzzle(new_sequence, new_values, test_fn)


# def test_puzzle(S: Sequence) -> bool:
#     # ab - cb = cd
#     return (10 * S[0] + S[1]) - (10 * S[2] + S[1]) == 10 * S[2] + S[3]


# solve_puzzle([], values=[1, 2, 3, 4], test_fn=test_puzzle)

"""
BCP 210 - Assignment 1: Arrays
University Course Registration Analytics
"""

from collections import Counter


def most_frequent(registrations):
    """Return the student ID that occurs most often.
    Time: O(n) | Space: O(n)
    """
    if not registrations:
        return None
    counts = Counter(registrations)
    return max(counts, key=counts.get)


def ordered_dedup(registrations):
    """Remove duplicates, keeping order of first appearance.
    Time: O(n) | Space: O(n)
    """
    seen = set()
    result = []
    for sid in registrations:
        if sid not in seen:
            seen.add(sid)
            result.append(sid)
    return result


def first_unique(registrations):
    """Return the first student ID that appears exactly once.
    Time: O(n) | Space: O(n)
    """
    counts = Counter(registrations)
    for sid in registrations:
        if counts[sid] == 1:
            return sid
    return None


def subarray_sum_exists(registrations, target):
    """Check if any contiguous subarray sums to target.
    Uses prefix-sum + hash set technique.
    Time: O(n) | Space: O(n)
    """
    prefix_sums = {0}
    running_sum = 0
    for value in registrations:
        running_sum += value
        if (running_sum - target) in prefix_sums:
            return True
        prefix_sums.add(running_sum)
    return False


def run_demo():
    registrations = [1023, 1050, 1023, 1102, 1050, 1023, 1201, 1102, 1300, 1023]
    target = 1050 + 1023 + 1201  # example target that exists as a contiguous sum

    print("Most frequent student:", most_frequent(registrations))
    print("Unique registrations:", ordered_dedup(registrations))
    print("First non-repeated student:", first_unique(registrations))
    print("Subarray with target sum exists:", subarray_sum_exists(registrations, target))


def run_tests():
    """Basic edge-case and typical-case tests."""
    assert most_frequent([]) is None
    assert most_frequent([5]) == 5
    assert most_frequent([1, 2, 2, 3]) == 2

    assert ordered_dedup([]) == []
    assert ordered_dedup([1, 1, 1]) == [1]
    assert ordered_dedup([1023, 1050, 1023, 1102]) == [1023, 1050, 1102]

    assert first_unique([]) is None
    assert first_unique([1, 1, 2, 2]) is None
    assert first_unique([1, 2, 2, 3]) == 1

    assert subarray_sum_exists([], 0) is False
    assert subarray_sum_exists([5], 5) is True
    assert subarray_sum_exists([1, 2, 3, 4], 9) is True
    assert subarray_sum_exists([1, 2, 3, 4], 100) is False

    print("All tests passed.")


if __name__ == "__main__":
    run_demo()
    print()
    run_tests()
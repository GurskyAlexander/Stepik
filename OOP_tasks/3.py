def inversions(sequence: list[int]) -> int:
    count = 0
    for i in range(len(sequence)):
        for j in range(i, len(sequence)):
            if sequence[i] > sequence[j]:
                count += 1
    return count


from collections import Counter


def find_unique_stone(gems):
    if len(gems) == 1:
        return len(gems[0])

    current = Counter(gems[0])

    for k, v in current.items():
        current[k] *= len(gems)
    for row in range(1, len(gems)):
        next_ = Counter(gems[row])
        remove = []
        for k, v in current.items():
            if k in next_ and current[k] - next_[k] >= 0:
                current[k] -= next_[k]
            else:
                remove.append(k)

        for r in remove:
            del current[r]

    return sum(current.values())


if __name__ == '__main__':
    print(find_unique_stone(["abcdde", "baccd", "eeabg"]))
    print(find_unique_stone(["dsd", "dd", "dd"]))
    print(find_unique_stone(["dsd"]))

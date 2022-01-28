import math
from math import sqrt


def evaluate(value, source: list):
    result = source[0]
    for i in range(1, len(source)):
        result += source[i] * math.pow(value, i)
    return result


def differentiate(source: list):
    result = []
    for i in range(1, len(source)):
        result.append(i * source[i])
    return result


def multiplicity_of_root(root, source: list):
    answer = 1
    current_source = source
    while len(current_source) != 1:
        current_source = differentiate(current_source)
        if evaluate(root, current_source) == 0:
            answer += 1
    return answer


def roots(source: list):
    free_coefficient = 0
    answer = []
    for element in source:
        if element != 0:
            free_coefficient = element
            break
    if free_coefficient != source[0]:
        answer.append(0)
    dividers = set()
    for i in range(1, int(sqrt(abs(free_coefficient))) + 1):
        if free_coefficient % i == 0:
            dividers.add(i)
            dividers.add(-i)
            if i * i != free_coefficient:
                dividers.add(free_coefficient / i)
                dividers.add(-free_coefficient / i)
    for divider in dividers:
        if evaluate(divider, source) == 0:
            for i in range(0, multiplicity_of_root(divider, source)):
                answer.append(divider)
    answer.sort(reverse=True)
    return answer


a = [-2, -3, 0, 1]  # => x^3 - 3x - 2
print(roots(a))

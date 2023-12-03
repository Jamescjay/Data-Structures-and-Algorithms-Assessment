def remove_duplicates(sequence):
    seen = set()
    result = []

    for element in sequence:
        if element not in seen:
            seen.add(element)
            result.append(element)

    return result

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
print(remove_duplicates(input_sequence))

# Case sensitive

def is_compressed(compressed,original):
    return len(compressed) < len(original)

def compressor(string, case_insensitive):
    true_string = string
    if case_insensitive:
        true_string = string.lower()

    collected_arrays = [[true_string[0]]]

    for n in range(1, len(true_string)):

        if true_string[n] == true_string[n-1]:
            collected_arrays[-1].append(true_string[n])
            # add to last array inside of collected_arrays
        elif true_string[n] != true_string[n-1]:
            # add to last array in collected_arrays
            # add another array to collected_arrays
            collected_arrays.append([true_string[n]])

    compressed_arrays = []

    for grouped_letters in collected_arrays:
            letter = grouped_letters[0]
            count = len(grouped_letters)
            compressed_arrays.append(letter + str(count))

    compressed_string = (''.join(compressed_arrays))

    if is_compressed(compressed_string, true_string):
        return(compressed_string)
    else:
        return(true_string)

print(compressor('aabBBbccCCCCCCCCccdaa', True))
print(compressor('aabBBbccCCCCCCCCccdaa', False))

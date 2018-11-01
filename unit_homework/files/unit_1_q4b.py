# Case INsensitive
def is_compressed(compressed,original):
    return len(compressed) < len(original)

string = 'aabBBbccccdaa'
string_clean = string.lower()
collected_arrays = [[string[0]]]

for n in range(1, len(string_clean)):
    if string_clean[n] == string_clean[n-1]:
        collected_arrays[-1].append(string_clean[n])
        # add to last array inside of collected_arrays
    elif string_clean[n] != string_clean[n-1]:
        # add to last array in collected_arrays
        # add another array to collected_arrays
        collected_arrays.append([string_clean[n]])

# create array of arrays and concatenate
compressed_arrays = []

for grouped_letters in collected_arrays:
        letter = grouped_letters[0]
        count = len(grouped_letters)
        compressed_arrays.append(letter + str(count))

compressed_string = (''.join(compressed_arrays))

if is_compressed(compressed_string, string):
    print(compressed_string)
else:
    print(string)

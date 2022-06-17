
def get_longest_seq(seq):
    pre_index = 0
    current_index = 1
    lst_test = []
    len_seqs = [1] * len(seq)
    while(len(seq) > current_index):
        if seq[pre_index] < seq[current_index]:
            new_len = len_seqs[pre_index] + 1
            if new_len > len_seqs[current_index]:
                len_seqs[current_index] = new_len

        pre_index += 1
        if pre_index == current_index:
            pre_index = 0
            current_index += 1

    longest_len = 0

    for val in len_seqs:
        if val > longest_len:
            longest_len = val

    return longest_len

d = get_longest_seq([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15])

print(d)

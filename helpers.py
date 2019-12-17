from nltk.tokenize import sent_tokenize, word_tokenize

def lines(a, b):
    """Return lines in both a and b"""
    A = a.split("\n")
    B = b.split("\n")
    final_list = []
    for i in A:
        if i in B and i not in final_list and i != '':
            final_list.append(i)
    return final_list


def sentences(a, b):
    """Return sentences in both a and b"""
    A = sent_tokenize(a)
    B = sent_tokenize(b)
    final_list = []
    for i in A:
        if i in B and i not in final_list:
            final_list.append(i)
    return final_list


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""
    A = [words for words in word_tokenize(a)]
    B = [words for words in word_tokenize(b)]
    A_substrings = []
    B_substrings = []
    final_list = []

    for words in A:
        counter = 0
        while (counter+n) <= (len(words)):
            A_substrings.append(words[counter:(counter+n)])
            counter += 1



    for words in B:
        counter = 0
        while (counter+n) <= (len(words)):
            B_substrings.append(words[counter:(counter+n)])
            counter += 1

    for substring in A_substrings:
        if substring in B_substrings and substring not in final_list:
            final_list.append(substring)

    return final_list

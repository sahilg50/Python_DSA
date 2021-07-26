string = ['rstax', 'rstax', 'gebi', 'gebi', 'rstax',
          'tgpj', 'tgpj', 'tgpj', 'gebi', 'rstax', 'tgpj']


def mostFrequentWord(arr, n):
    # code here
    word_frequency = {}
    for i in range(len(arr)):
        if arr[i] in word_frequency:
            word_frequency[arr[i]] += 1
        else:
            word_frequency[arr[i]] = 1

    key = ""
    value = 0

    for K, V in word_frequency.items():
        if(V >= value):
            value = V
            key = K

    return key


answer = mostFrequentWord(string, 11)
print(answer)

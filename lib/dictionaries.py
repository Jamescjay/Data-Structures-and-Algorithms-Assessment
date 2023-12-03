import string

def word_frequency(sentence):
    
    translator = str.maketrans("", "", string.punctuation)
    new_sentence = sentence.translate(translator).lower()

    words = new_sentence.split()

    frequency_dict = {}
    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
def get_num_words(text):
    words = text.split()
    return len(words)


def get_count_characters(text):
    results = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            if char in results:
                results[char] += 1
            else:
                results[char] = 1
    return results
def single_root_words(root_word, *other_words):
    same_words = []
    words = list(other_words)
    for i in range(len(words)):
        words[i] = words[i].lower()
        root_word = root_word.lower()
        if root_word in words[i] or words[i] in root_word:
            same_words.append(words[i])

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

def total_words(book):
    return len(book.split())

def letter_count(book):
    letters = {}
    words = book.split()
    for word in words:
        for letter in word:
            if letter.lower() in letters:
                letters[letter.lower()] += 1
            else:
                letters[letter.lower()] = 1
    return letters

def letter_sort(letters_count):
    letter_count_list = []
    for key in letters_count:
        char = key
        num = letters_count[key]
        entry = {'char':char, 'num':num}
        letter_count_list.append(entry)
    letter_count_list.sort(reverse=True, key=sort_on)
    return letter_count_list

def sort_on(items):
    return items["num"]

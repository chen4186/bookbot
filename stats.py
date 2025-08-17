def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def count_characters(text):
    count_dict = {}
    text_lower = text.lower()
    for char in text_lower:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1

    return count_dict

def create_dict_list(item):
    new_list = []
    for key, value in item.items():
        if key.isalpha():
            new_list.append({"char": key, "count": value})

    new_list.sort(reverse=True, key=sort_on)

    return new_list

def sort_on(item):
    return item["count"]

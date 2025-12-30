def get_num_words(text: str) -> int:
    return len(text.split())


def get_char_freq(text: str) -> dict[str, int]:
    freq_dict = {}
    for c in text.lower():
        if c not in freq_dict.keys():
            freq_dict[c] = 1
        else:
            freq_dict[c] += 1
    return freq_dict


def to_sorted_list_of_dicts(freq_dict: dict[str, int]) -> list[dict[str, int]]:
    
    def sort_on(items):
        return items["num"]

    list_of_dicts = [{"char": key, "num": val} for key, val in freq_dict.items()]
    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts

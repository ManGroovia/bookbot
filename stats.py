def word_count(text):
    splited = text.split()
    count = len(splited)
    return count

def symb_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return [{'char': k, 'num': v} for k, v in char_dict.items()]      


    




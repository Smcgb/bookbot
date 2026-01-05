def word_count(book_text: str) -> str:
    
    return f"Found {len(book_text.split())} total words"

def letter_char_count(book_text: str) -> dict[str, int]:

    letter_count = {}
   
    for word in book_text.lower().split():
            for letter in word:
                    if letter.isalpha():
                        if letter not in letter_count:
                            letter_count[letter] = 0
                        letter_count[letter] += 1

    return letter_count

def sort_on(items):
    return items["num"]

def sorted_list_of_char_count(letter_count: dict) -> list:

    sorted_letter_counts = []

    for k, v in letter_count.items():
        sorted_letter_counts.append({'name': k, "num": v})

    sorted_letter_counts.sort(reverse=True, key=sort_on)

    return sorted_letter_counts

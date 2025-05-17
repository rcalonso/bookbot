
def get_num_words(data: str):
    words = data.split()
    return len(words)

def get_chars_distribution(data: str):
    counter = {}
    for c in data:
        lower_char = c.lower()
        if lower_char not in counter:
            counter[lower_char] = 1
        else:
            counter[lower_char] += 1
    return counter


def get_stats_list(chars_stats: dict):
    summary = []
    for char, num in chars_stats.items():
        summary.append(
            {
                "char": char,
                "num": num
            }
        )
    summary.sort(key=lambda x: x["num"], reverse=True)
    return summary

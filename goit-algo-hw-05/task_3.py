import timeit


def measure_time(func, text, pattern, repeats=10):
    timer = timeit.Timer(lambda: func(text, pattern))
    total = timer.timeit(number=repeats)
    return total / repeats


def build_shift_table(pattern):
    table = {}
    length = len(pattern)
    for index, char in enumerate(pattern[:-1]):
        table[char] = length - index - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text, pattern):
    shift_table = build_shift_table(pattern)
    i = 0

    while i <= len(text) - len(pattern):
        j = len(pattern) - 1

        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i  # Підрядок знайдено
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return -1


def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def kmp_search(main_string, pattern):
    M = len(pattern)
    N = len(main_string)

    lps = compute_lps(pattern)

    i = j = 0

    while i < N:
        if pattern[j] == main_string[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1

        if j == M:
            return i - j

    return -1


def polynomial_hash(s, base=256, modulus=101):
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def rabin_karp_search(main_string, substring):
    substring_length = len(substring)
    main_string_length = len(main_string)

    base = 256
    modulus = 101

    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    h_multiplier = pow(base, substring_length - 1) % modulus

    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash:
            if main_string[i:i + substring_length] == substring:
                return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus
            if current_slice_hash < 0:
                current_slice_hash += modulus

    return -1


def average(values):
    return sum(values) / len(values)


def best_time_for_algorithm(avg_times_dict):
    return min(avg_times_dict, key=avg_times_dict.get)


with open("стаття 1.txt", "r", encoding="utf-8") as f:
    text_1 = f.read()

with open("стаття 2 (1).txt", "r", encoding="utf-8") as f:
    text_2 = f.read()

pattern_1 = "пошук"
pattern_2 = "що-небудь"
patterns = [("pattern_1", pattern_1), ("pattern_2", pattern_2)]

texts = [("text_1", text_1), ("text_2", text_2)]

collection_of_results = {
    "text_1": {"BM": [], "KMP": [], "RK": []},
    "text_2": {"BM": [], "KMP": [], "RK": []},
}

for text_name, text in texts:
    print(f'Results for {text_name}:')
    for pattern_name, pattern in patterns:
        if pattern in text:
            print(f'Using the {pattern_name}:')
        else:
            print(f'There is no {pattern_name} in text, but we spend time for searching:')

        bm_time = measure_time(boyer_moore_search, text, pattern)
        kmp_time = measure_time(kmp_search, text, pattern)
        rk_time = measure_time(rabin_karp_search, text, pattern)

        print(f"    Boyer-Moore : {bm_time:.6f}")
        print(f"    KMP         : {kmp_time:.6f}")
        print(f"    Rabin-Karp  : {rk_time:.6f}")

        collection_of_results[text_name]["BM"].append(bm_time)
        collection_of_results[text_name]["KMP"].append(kmp_time)
        collection_of_results[text_name]["RK"].append(rk_time)

best_by_text = {}

for text_name, algo_dict in collection_of_results.items():
    avr_time = {}

    for algo_name, algo_time in algo_dict.items():
        avr_time[algo_name] = average(algo_time)

    best_result = best_time_for_algorithm(avr_time)
    best_by_text[text_name] = (best_result, avr_time[best_result])

overall_avg = {}
for algo_name in ["BM", "KMP", "RK"]:
    list_of_time = []
    for text_name in collection_of_results:
        times_for_text = collection_of_results[text_name][algo_name]
        list_of_time.extend(times_for_text)

    overall_avg[algo_name] = average(list_of_time)

best_overall_avg = best_time_for_algorithm(overall_avg)

print("\n=== Best by text ===")
for text_name, (best_algo, best_time) in best_by_text.items():
    print(f"{text_name}: {best_algo} ({best_time:.6f} s)")

print("\n=== Overall average ===")
print(overall_avg)
print("Best overall:", best_overall_avg, f"({overall_avg[best_overall_avg]:.6f} s)")


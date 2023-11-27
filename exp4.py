def is_mapping_possible(arr, target):
    def is_valid_mapping(mapping, encoded_str):
        mapped_value = int("".join(str(mapping[char]) for char in encoded_str))
        return mapped_value == target

    def backtrack(index, mapping, used_digits):
        if index == len(unique_chars):
            # Check if the mapping satisfies the condition
            if is_valid_mapping(mapping, target):
                return True
            return False

        char = unique_chars[index]
        for digit in range(10):
            if digit not in used_digits:
                mapping[char] = digit
                used_digits.add(digit)
                if backtrack(index + 1, mapping, used_digits):
                    return True
                mapping[char] = -1  # Backtrack
                used_digits.remove(digit)

        return False

    unique_chars = set("".join(arr) + target)
    if len(unique_chars) > 10:
        return False  # More than 10 unique characters, not possible to map

    mapping = {char: -1 for char in unique_chars}
    used_digits = set()
    return backtrack(0, mapping, used_digits)

# Example
arr = ["SEND", "MORE"]
target = "MONEY"
result = is_mapping_possible(arr, int(target))
print("Output:", "Yes" if result else "No")

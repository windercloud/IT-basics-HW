def unique_key_values(input_dict):
    seen_values = set()
    return {key: value for key, value in input_dict.items() if not (value in seen_values or seen_values.add(value))}

if __name__ == "__main__":
    sample_dict = { "a": 1, "b": 2, "c": 3, "d": 2, "e": 4, "f": 1 }
    
    unique_entries = unique_key_values(sample_dict)
    print("Уникальные значения:", unique_entries)
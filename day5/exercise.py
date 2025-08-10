# def merge_with_conflict_handling(dict1: dict, dict2: dict) -> dict:
    
#     merged = dict1.copy()

#     for key, value in dict2.items():
#         if (existing := merged.get(key)) is not None:
#             print(f"Conflict for key '{key}': dict1 has {existing}, dict2 has {value}")
#         merged[key] = value  # Use value from dict2 regardless

#     return merged


# if __name__ == "__main__":
#     dict1 = {"name": "Alice", "age": 25, "city": "Amman"}
#     dict2 = {"age": 30, "country": "Jordan", "city": "Irbid"}

#     result = merge_with_conflict_handling(dict1, dict2)
#     print("\nMerged dictionary:", result)

    
ditc3 = {'name':'1'}

if x := ditc3.get('nameera'):
    print("1111111111")
    print(x)
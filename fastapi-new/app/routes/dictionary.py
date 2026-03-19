from fastapi import APIRouter

router = APIRouter(prefix="/dict", tags=["Dictionary Exercises"])


# 🟢 1. Create & access
@router.get("/basic")
async def basic_dict():
    data = {"name": "Rohith", "age": 25}
    return {"name": data["name"], "age": data["age"]}


# 🟢 2. Add key-value
@router.get("/add")
async def add_item():
    data = {"a": 1, "b": 2}
    data["c"] = 3
    return data


# 🟢 3. Update value
@router.get("/update")
async def update_item():
    data = {"a": 1, "b": 2}
    data["a"] = 100
    return data


# 🟢 4. Remove key
@router.get("/remove")
async def remove_item():
    data = {"a": 1, "b": 2, "c": 3}
    data.pop("b")
    return data


# 🟡 5. Get keys & values
@router.get("/keys-values")
async def keys_values():
    data = {"a": 1, "b": 2}
    return {"keys": list(data.keys()), "values": list(data.values())}


# 🟡 6. Check key exists
@router.get("/exists")
async def check_key():
    data = {"a": 1, "b": 2}
    return {"has_a": "a" in data}


# 🟡 7. Merge dictionaries
@router.get("/merge")
async def merge_dicts():
    a = {"x": 1}
    b = {"y": 2}
    return {**a, **b}


# 🟠 8. Count frequency (important)
@router.get("/frequency")
async def frequency():
    data = [1, 1, 2, 3, 2, 1]
    freq = {}
    for n in data:
        freq[n] = freq.get(n, 0) + 1
    return freq


# 🟠 9. Nested dictionary
@router.get("/nested")
async def nested_dict():
    data = {"user": {"name": "Rohith", "age": 25}}
    return data["user"]["name"]


# 🟠 10. Sort dictionary by value
@router.get("/sort")
async def sort_dict():
    data = {"a": 3, "b": 1, "c": 2}
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))
    return sorted_data


# 🔴 11. Invert dictionary
@router.get("/invert")
async def invert_dict():
    data = {"a": 1, "b": 2}
    return {v: k for k, v in data.items()}


# 🔴 12. Find max value key
@router.get("/max-key")
async def max_key():
    data = {"a": 10, "b": 50, "c": 30}
    return max(data, key=data.get)


# 🔴 13. Group elements (advanced)
@router.get("/group")
async def group_items():
    data = ["apple", "ant", "banana", "bat"]
    result = {}
    for word in data:
        key = word[0]
        result.setdefault(key, []).append(word)
    return result

from fastapi import APIRouter

router = APIRouter(prefix="/tuples", tags=["Tuple Exercises"])


# 🟢 1. Create & access tuple
@router.get("/basic")
async def basic_tuple():
    data = (10, 20, 30, 40)
    return {
        "first": data[0],
        "last": data[-1]
    }


# 🟢 2. Length of tuple
@router.get("/length")
async def tuple_length():
    data = ("a", "b", "c")
    return {"length": len(data)}


# 🟢 3. Convert list → tuple
@router.get("/list-to-tuple")
async def list_to_tuple():
    data = [1, 2, 3]
    return tuple(data)


# 🟡 4. Convert tuple → list (modify)
@router.get("/tuple-to-list")
async def tuple_to_list():
    data = (1, 2, 3)
    temp = list(data)
    temp.append(4)
    return temp


# 🟡 5. Count occurrences
@router.get("/count")
async def count_value():
    data = (1, 2, 2, 3, 2)
    return {"count_of_2": data.count(2)}


# 🟡 6. Find index
@router.get("/index")
async def find_index():
    data = (10, 20, 30, 40)
    return {"index_of_30": data.index(30)}


# 🟠 7. Tuple unpacking
@router.get("/unpack")
async def unpack():
    data = (1, 2, 3)
    a, b, c = data
    return {"a": a, "b": b, "c": c}


# 🟠 8. Swap values using tuple
@router.get("/swap")
async def swap():
    a = 10
    b = 20
    a, b = b, a
    return {"a": a, "b": b}


# 🟠 9. Nested tuple access
@router.get("/nested")
async def nested():
    data = (1, (2, 3), 4)
    return {"inner_value": data[1][1]}  # 3


# 🔴 10. Remove duplicates (convert to set)
@router.get("/unique")
async def unique_tuple():
    data = (1, 2, 2, 3, 4, 4)
    return tuple(set(data))


# 🔴 11. Max & Min
@router.get("/min-max")
async def min_max():
    data = (5, 1, 9, 3)
    return {
        "min": min(data),
        "max": max(data)
    }


# 🔴 12. Sum of tuple
@router.get("/sum")
async def tuple_sum():
    data = (1, 2, 3, 4)
    total = 0
    for n in data:
        total += n
    return {"sum": total}
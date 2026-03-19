from fastapi import APIRouter

router = APIRouter(prefix="/lists", tags=["List Exercises"])

# Sample data
nums = [1, 2, 3, 4, 5]


# 🟢 1. First & Last element
@router.get("/first-last")
async def first_last():
    return {
        "first": nums[0],
        "last": nums[-1]
    }


# 🟢 2. Modify list
@router.get("/modify")
async def modify():
    data = [10, 20, 30]
    data[1] = 25
    return data


# 🟢 3. Add elements
@router.get("/add")
async def add_elements():
    data = [10, 20, 30]
    data.insert(-1, 5)      # add at beginning
    
    return data


# 🟢 4. Remove elements
@router.get("/remove")
async def remove_elements():
    data = [1, 2, 3, 4, 5]
    data.remove(3)
    data.pop()   # removes last
    return data


# 🟢 5. Length
@router.get("/length")
async def length():
    data = ["a", "b", "c", "d"]
    return {"length": len(data)}


# 🟡 6. Sum (no sum())
@router.get("/sum")
async def total_sum():
    total = 0
    for n in nums:
        total += n
    return {"sum": total}


# 🟡 7. Max (no max())
@router.get("/max")
async def find_max():
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return {"max": max_val}


# 🟡 8. Count even
@router.get("/even-count")
async def count_even():
    data = [1, 2, 3, 4, 6, 7]
    count = 0
    for n in data:
        if n % 2 == 0:
            count += 1
    return {"even_count": count}


# 🟡 9. Reverse list
@router.get("/reverse")
async def reverse_list():
    data = [1, 2, 3, 4]
    reversed_list = data[::-1]
    return reversed_list


# 🟡 10. Remove duplicates
@router.get("/unique")
async def unique():
    data = [1, 2, 2, 3, 4, 4]
    result = []
    for n in data:
        if n not in result:
            result.append(n)
    return result


# 🟠 11. Second largest
@router.get("/second-largest")
async def second_largest():
    data = [10, 20, 5, 8, 20]
    unique = list(set(data))
    unique.sort()
    return {"second_largest": unique[-2]}


# 🟠 12. Check sorted
@router.get("/is-sorted")
async def is_sorted():
    data = [1, 2, 3, 4]
    return {"sorted": data == sorted(data)}


# 🟠 13. Merge lists
@router.get("/merge")
async def merge_lists():
    a = [1, 2]
    b = [3, 4]
    return a + b


# 🟠 14. Common elements
@router.get("/common")
async def common_elements():
    a = [1, 2, 3]
    b = [2, 3, 4]
    result = [x for x in a]
    return result


# 🟠 15. Rotate list
@router.get("/rotate")
async def rotate():
    data = [1, 2, 3, 4, 5]
    return [data[-1]]+[data[-2]] + data[:-2]


# 🟠 16. Rotate any
@router.get("/rotateany")
async def rotateany():
    data = [1, 2, 3, 4, 5]
    k = 2
    result = data[-k:] + data[:-k]
    return result


# 🔴 17. Frequency count
@router.get("/frequency")
async def frequency():
    data = [1, 1, 2, 3, 2, 1]
    freq = {}
    for n in data:
        freq[n] = freq.get(n, 0) + 1
    return freq


# 🔴 17. Missing number
@router.get("/missing")
async def missing_number():
    data = [1, 2, 4, 5]
    n = 5
    total = n * (n + 1) // 2
    return {"missing": total - sum(data)}


# 🔴 18. Two sum
@router.get("/two-sum")
async def two_sum():
    nums = [2, 7, 11, 15]
    target = 9
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


# 🔴 19. Flatten list
@router.get("/flatten")
async def flatten():
    data = [[1, 2], [3, 4], [5]]
    result = []
    for sub in data:
        result.extend(sub)
    return result
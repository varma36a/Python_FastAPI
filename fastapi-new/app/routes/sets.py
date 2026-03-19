from fastapi import APIRouter

router = APIRouter(prefix="/sets", tags=["Set Exercises"])


# 🟢 1. Create set & uniqueness
@router.get("/basic")
async def basic_set():
    data = [1, 2, 2, 3, 4]
    return list(set(data))  # removes duplicates


# 🟢 2. Add element
@router.get("/add")
async def add_element():
    s = {1, 2, 3}
    s.add(4)
    return list(s)


# 🟢 3. Remove element
@router.get("/remove")
async def remove_element():
    s = {1, 2, 3, 4}
    s.remove(2)
    return list(s)


# 🟡 4. Union
@router.get("/union")
async def union_sets():
    a = {1, 2, 3}
    b = {3, 4, 5}
    return list(a.union(b))


# 🟡 5. Intersection
@router.get("/intersection")
async def intersection_sets():
    a = {1, 2, 3}
    b = {2, 3, 4}
    return list(a.intersection(b))


# 🟡 6. Difference
@router.get("/difference")
async def difference_sets():
    a = {1, 2, 3}
    b = {2, 3, 4}
    return list(a.difference(b))  # elements in a not in b


# 🟠 7. Symmetric difference
@router.get("/symmetric-diff")
async def symmetric_diff():
    a = {1, 2, 3}
    b = {3, 4, 5}
    return list(a.symmetric_difference(b))


# 🟠 8. Check subset
@router.get("/subset")
async def subset():
    a = {1, 2}
    b = {1, 2, 3}
    return {"is_subset": a.issubset(b)}


# 🟠 9. Check superset
@router.get("/superset")
async def superset():
    a = {1, 2, 3}
    b = {1, 2}
    return {"is_superset": a.issuperset(b)}


# 🔴 10. Remove duplicates from list (real use case)
@router.get("/deduplicate")
async def deduplicate():
    data = [1, 1, 2, 3, 3, 4]
    return list(set(data))


# 🔴 11. Common elements (intersection real case)
@router.get("/common")
async def common():
    a = [1, 2, 3]
    b = [2, 3, 4]
    return list(set(a) & set(b))


# 🔴 12. Unique elements across lists
@router.get("/unique-all")
async def unique_all():
    a = [1, 2, 3]
    b = [3, 4, 5]
    return list(set(a) | set(b))

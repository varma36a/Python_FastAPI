from fastapi import APIRouter

router = APIRouter(prefix="/logic", tags=["Functions & Loops"])


# 🟢 1. Simple function
def add(a, b):
    return a + b


@router.get("/add")
async def add_api():
    return {"result": add(5, 3)}


# 🟢 2. Function with loop (sum)
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total


@router.get("/sum")
async def sum_api():
    data = [1, 2, 3, 4]
    return {"sum": sum_list(data)}


# 🟢 3. Loop example (even numbers)
@router.get("/evens")
async def even_numbers():
    data = [1, 2, 3, 4, 5, 6]
    evens = []
    for n in data:
        if n % 2 == 0:
            evens.append(n)
    return evens


# 🟡 4. Factorial using loop
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


@router.get("/factorial")
async def factorial_api():
    return {"factorial": factorial(5)}


# 🟡 5. Reverse string using loop
def reverse_string(s):
    result = ""
    for char in s:
        result = char + result
    return result


@router.get("/reverse")
async def reverse_api():
    return {"reversed": reverse_string("hello")}


# 🟡 6. Count vowels
def count_vowels(s):
    vowels = "aeiou"
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    return count


@router.get("/vowels")
async def vowels_api():
    return {"count": count_vowels("FastAPI")}


# 🟠 7. Find max using function
def find_max(nums):
    max_val = nums[0]
    for n in nums:
        if n > max_val:
            max_val = n
    return max_val


@router.get("/max")
async def max_api():
    return {"max": find_max([10, 50, 20])}


# 🟠 8. Prime number check
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


@router.get("/prime")
async def prime_api():
    return {"is_prime": is_prime(7)}


# 🟠 9. Multiplication table
@router.get("/table")
async def table():
    n = 5
    result = []
    for i in range(1, 11):
        result.append(f"{n} x {i} = {n*i}")
    return result


# 🔴 10. Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


@router.get("/fibonacci")
async def fibonacci_api():
    return fibonacci(7)


# 🔴 11. Count frequency using loop + dict
@router.get("/frequency")
async def frequency_api():
    data = [1, 1, 2, 3, 2, 1]
    freq = {}
    for n in data:
        freq[n] = freq.get(n, 0) + 1
    return freq

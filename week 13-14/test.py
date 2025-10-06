import random
import time
from dataclasses import dataclass

@dataclass
class Stats:
    comparisons: int = 0
    writes: int = 0
    elapsed_ms: float = 0.0

def bubble_sort(a):
    arr = a[:]
    n = len(arr)
    st = Stats()
    t0 = time.perf_counter()
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            st.comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                st.writes += 3
                swapped = True
        if not swapped:
            break
    st.elapsed_ms = (time.perf_counter() - t0) * 1000
    return arr, st

def selection_sort(a):
    arr = a[:]
    n = len(arr)
    st = Stats()
    t0 = time.perf_counter()
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            st.comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            st.writes += 3
    st.elapsed_ms = (time.perf_counter() - t0) * 1000
    return arr, st

def insertion_sort(a):
    arr = a[:]
    st = Stats()
    t0 = time.perf_counter()
    for i in range(1, len(arr)):
        key = arr[i]
        st.writes += 1
        j = i - 1
        while j >= 0:
            st.comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                st.writes += 1
                j -= 1
            else:
                break
        arr[j + 1] = key
        st.writes += 1
    st.elapsed_ms = (time.perf_counter() - t0) * 1000
    return arr, st

def check_correctness():
    algos = [("Bubble", bubble_sort), ("Selection", selection_sort), ("Insertion", insertion_sort)]
    for _ in range(50):
        data = [random.randint(-999, 999) for _ in range(random.randint(0, 50))]
        expected = sorted(data)
        for name, fn in algos:
            got, _ = fn(data)
            assert got == expected, f"{name} failed on {data}"
    return "All algorithms match built-in sorted()"

def small_demo():
    data = [12, 5, 9, 1, 12, 7]
    print("Original:", data)
    for name, fn in [("Bubble", bubble_sort), ("Selection", selection_sort), ("Insertion", insertion_sort)]:
        out, st = fn(data)
        print(f"{name:9s} -> {out} | comps={st.comparisons:,} writes={st.writes:,} time={st.elapsed_ms:.3f} ms")

def benchmark():
    sizes = [100, 300, 600, 900]
    print("\n=== Benchmark (random ints) ===")
    print(f"{'n':>5} | {'Algo':9s} | {'ms':>8} | {'comparisons':>12} | {'writes':>10}")
    print("-" * 56)
    for n in sizes:
        data = [random.randint(-10000, 10000) for _ in range(n)]
        for name, fn in [("Bubble", bubble_sort), ("Selection", selection_sort), ("Insertion", insertion_sort)]:
            _, st = fn(data)
            print(f"{n:5d} | {name:9s} | {st.elapsed_ms:8.2f} | {st.comparisons:12,d} | {st.writes:10,d}")

# ฟังก์ชันใหม่ตามเมนูในภาพ
def custom_or_random_data(n):
    print(f"\n1. กำหนด/สุ่ม Data แบบ {n} ตัว")
    choice = input("คุณต้องการ (1) กำหนดเอง หรือ (2) สุ่มข้อมูล? ใส่เลข 1 หรือ 2: ").strip()
    if choice == "1":
        raw = input(f"ป้อนตัวเลข {n} ค่า คั่นด้วยช่องว่าง: ")
        data = list(map(int, raw.strip().split()))
        if len(data) != n:
            print(f"จำนวนข้อมูลไม่ตรงกับ {n} ตัว ใช้เฉพาะตัวแรก {n} ตัว")
            data = data[:n]
    else:
        min_val = int(input("ค่าต่ำสุด: "))
        max_val = int(input("ค่าสูงสุด: "))
        data = [random.randint(min_val, max_val) for _ in range(n)]
    return data

def custom_or_random_sizes():
    print("2. กำหนด/สุ่ม Sizes แบบ n ตัว")
    choice = input("คุณต้องการ (1) กำหนดเอง หรือ (2) สุ่มขนาด? ใส่เลข 1 หรือ 2: ").strip()
    if choice == "1":
        raw = input("ป้อนขนาด (จำนวนเต็มหลายค่า) เช่น 50 100 200: ")
        sizes = list(map(int, raw.strip().split()))
    else:
        count = int(input("จำนวนขนาดที่ต้องการสุ่ม: "))
        min_size = int(input("ขนาดต่ำสุด: "))
        max_size = int(input("ขนาดสูงสุด: "))
        sizes = [random.randint(min_size, max_size) for _ in range(count)]
    return sizes

def user_driven_benchmark():
    sizes = custom_or_random_sizes()
    print("\n=== Benchmark (custom/random data) ===")
    print(f"{'n':>5} | {'Algo':9s} | {'ms':>8} | {'comparisons':>12} | {'writes':>10}")
    print("-" * 56)
    for n in sizes:
        data = custom_or_random_data(n)
        for name, fn in [("Bubble", bubble_sort), ("Selection", selection_sort), ("Insertion", insertion_sort)]:
            _, st = fn(data)
            print(f"{n:5d} | {name:9s} | {st.elapsed_ms:8.2f} | {st.comparisons:12,d} | {st.writes:10,d}")

# main program
if __name__ == "__main__":
    print(check_correctness())
    small_demo()
    benchmark()
    
    print("\n--- เมนูจากภาพ ---")
    user_driven_benchmark()

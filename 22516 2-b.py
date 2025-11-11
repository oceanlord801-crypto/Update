employees = [
    {"id": 2, "name": "jyotiraditya", "salary": 20000},
    {"id": 3, "name": "kunal", "salary": 40000},
    {"id": 4, "name": "kundan", "salary": 60000},
    {"id": 6, "name": "dasrath", "salary": 80000},
    {"id": 8, "name": "om", "salary": 100000},
    {"id": 10, "name": "sandip", "salary": 120000},
    {"id": 12, "name": "adwait", "salary": 140000},
    {"id": 14, "name": "shivraj", "salary": 160000},
    {"id": 76, "name": "shiva", "salary": 10000000},
    {"id": 23, "name": "vedang", "salary": 500},
]


def quicksort(data):
    if len(data) <= 1:
        return data
    pivot = data[0]
    left = [x for x in data[1:] if x["id"] < pivot["id"]]
    right = [x for x in data[1:] if x["id"] >= pivot["id"]]
    return quicksort(left) + [pivot] + quicksort(right)


def mergesort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = mergesort(data[:mid])
    right = mergesort(data[mid:])
    result = []
    while left and right:
        result.append(
            left.pop(0) if left[0]["name"] < right[0]["name"] else right.pop(0)
        )
       return result + left + right


print("Sorted by ID(Quicksort):")
for emp in quicksort(employees):
    print(emp)

print("\nSorted by Name(MergeSort):")
for emp in mergesort(employees):
    print(emp)

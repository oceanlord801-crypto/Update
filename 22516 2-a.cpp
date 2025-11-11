students = [
    {"roll_no": 33, "name": "Jyotir", "sgpa": 8.36},
    {"roll_no": 34, "name": "Om", "sgpa": 7.15},
    {"roll_no": 42, "name": "kundan", "sgpa": 7.86},
    {"roll_no": 51, "name": "dasrath", "sgpa": 7.80},
    {"roll_no": 21, "name": "prithviraj", "sgpa": 8.38},
    {"roll_no": 68, "name": "Pradeep", "sgpa": 8.89},
    {"roll_no": 11, "name": "Ronaldo", "sgpa": 7.0},
    {"roll_no": 10, "name": "Messi", "sgpa": 9.0},
    {"roll_no": 9, "name": "Donhi", "sgpa": 8.99},
    {"roll_no": 2, "name": "vedang", "sgpa": 10.00},
]


def insertion_sort(arr, key):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > current[key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


insertion_sort(students, "roll_no")
print("Sorted by roll number:")
for s in students:
    print(s)

insertion_sort(students, "name")
print("\nSorted by name:")
for s in students:
    print(s)


def insertion_sort_desc(arr, key):
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] < current[key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


insertion_sort_desc(students, "sgpa")
top_5 = students[:5]

print("\nTop 5 students by sgpa:")
for s in top_5:
    print(s)

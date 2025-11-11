class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # each index stores a list

    def hash_function(self, key):
        return key % self.size

    def insert(self, emp_id, name):
        index = self.hash_function(emp_id)
        self.table[index].append((emp_id, name))

    def search(self, emp_id):
        index = self.hash_function(emp_id)
        for record in self.table[index]:
            if record[0] == emp_id:
                return record[1]
        return None

    def display(self):
        print("\nHash Table (Chaining):")
        for i in range(self.size):
            print(i, ":", self.table[i])


# Hash Table using LINEAR PROBING
class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, emp_id, name):
        index = self.hash_function(emp_id)
        while self.table[index] is not None:
            index = (index + 1) % self.size  # move to next index (collision handled)
        self.table[index] = (emp_id, name)

    def search(self, emp_id):
        index = self.hash_function(emp_id)
        start = index
        while self.table[index] is not None:
            if self.table[index][0] == emp_id:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == start:
                break
        return None

    def display(self):
        print("\nHash Table (Linear Probing):")
        for i in range(self.size):
            print(i, ":", self.table[i])


# -------------------------------
# Example Usage
# -------------------------------
chaining = HashTableChaining(5)
linear = HashTableLinearProbing(5)

# Insert employee records (id, name)
data = [(11, "Alice"), (22, "Bob"), (33, "Charlie"), (44, "David"), (15, "Eve")]

for emp_id, name in data:
    chaining.insert(emp_id, name)
    linear.insert(emp_id, name)

# Display tables
chaining.display()
linear.display()

# Search examples
print("\nSearch ID 22 using Chaining:", chaining.search(22))
print("Search ID 22 using Linear Probing:", linear.search(22))

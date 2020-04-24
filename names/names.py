import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
class BinarySearchTreeNames:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTreeNames(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNames(value)

    def contains(self, target):
        if target < self.value:
            if self.left:
                self.left.contains(target)
            else:
                pass
        if target > self.value:
            if self.right:
                self.right.contains(target)
            else:
                pass
        if target == self.value:
            duplicates.append(target)


names_3 = ['John', "Jerry", "Amy", "Doug", "Casey", "Will"]
names_4 = ['Amy', 'Mike', "Luke", 'Rask', 'Will']
N = BinarySearchTreeNames("first")
for name in names_1:
    N.insert(name)

for name in names_2:
    N.contains(name)



end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

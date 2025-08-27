🔹 Dictionary Codes in Python
🟢 Basic Level (1–7)
1. Create a Dictionary
student = {"name": "Surendra", "age": 21, "course": "Python"}
print(student)

2. Access Dictionary Values
print(student["name"])      # Access using key
print(student.get("age"))   # Using get() method

3. Add a New Key-Value Pair
student["grade"] = "A"
print(student)

4. Update Value
student["age"] = 22
print(student)

5. Delete a Key
del student["course"]
print(student)

6. Iterate through Dictionary
for key, value in student.items():
    print(key, ":", value)

7. Check if Key Exists
if "name" in student:
    print("Key exists!")

🟡 Intermediate Level (8–14)
8. Dictionary Length
print("Length:", len(student))

9. Nested Dictionary
students = {
    "101": {"name": "Surendra", "age": 21},
    "102": {"name": "Ravi", "age": 22}
}
print(students["101"]["name"])

10. Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)

11. Merge Two Dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)
print(dict1)

12. Get Keys and Values
print(student.keys())
print(student.values())

13. Copy a Dictionary
new_student = student.copy()
print(new_student)

14. Clear Dictionary
student.clear()
print(student)

🔴 Advanced Level (15–20)
15. Count Frequency of Elements
data = ["a", "b", "a", "c", "b", "a"]
freq = {}
for item in data:
    freq[item] = freq.get(item, 0) + 1
print(freq)

16. Sort Dictionary by Keys
d = {"b": 2, "a": 5, "c": 1}
sorted_dict = dict(sorted(d.items()))
print(sorted_dict)

17. Sort Dictionary by Values
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_dict)

18. Find Max and Min Value
d = {"a": 10, "b": 5, "c": 15}
print("Max:", max(d, key=d.get))
print("Min:", min(d, key=d.get))

19. Dictionary of Word Count
text = "python is easy and python is powerful"
words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

20. Convert Two Lists into Dictionary
keys = ["name", "age", "city"]
values = ["Surendra", 21, "Hyderabad"]
my_dict = dict(zip(keys, values))
print(my_dict)

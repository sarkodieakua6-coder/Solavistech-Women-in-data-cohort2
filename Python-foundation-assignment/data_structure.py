#.SECTION 4 : DATA STRUCTURES
#1.FAVORITE TOOLS LIST
print("FAVORITE TOOLS LIST :")
list_of_tools = ["Python", "Git", "Docker", "VS Code", "Linux"]
list_of_tools.append("SQL")
print("My favorite tools are : ", list_of_tools)
list_of_tools.remove("Docker")
print("Updated list of favorite tools : ", list_of_tools)


#2. STUDENT SCORES
print("STUDENT SCORES :")
student_scores = [20, 35, 50, 65, 80]
print("Highest score : ", max(student_scores))
print("Lowest score : ", min(student_scores))
print("Average score : ", sum(student_scores) / len(student_scores))

#3. SHOPPING LIST MANAGER
print("SHOPPING LIST MANAGER :")
shopping_list = []
shopping_list.append(input("Enter an item to add to the shopping list : "))
shopping_list.append(input("Enter another item to add to the shopping list : "))        
print("Current shopping list : ", shopping_list)
item_to_remove = input("Enter an item to remove from the shopping list : ")
if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print("Updated shopping list : ", shopping_list)
else:
    print("Item not found in the shopping list.")
    

#4. CONTRY CAPITALS
print("COUNTRY CAPITALS :")
country_capitals = (("Ghana", "Accra"), ("Nigeria", "Abuja"), ("Kenya", "Nairobi"), ("South Africa", "Pretoria"), ("Egypt", "Cairo"))
print("Country and their capitals : ", country_capitals)
for country, capital in country_capitals:
    print(f"The capital of {country} is {capital}.")
    


#5. UNIQUE VISITORS
print("UNIQUE VISITORS :")
unique_visitors = [ "Danny", "Sarah", "Mike", "Danny", "Lisa", "Sarah" ]
unique_visitors_set = set(unique_visitors)
print("Unique visitors : ", unique_visitors_set)


#6. COMMON SKILLS
print("COMMON SKILLS :")
skills_set1 = {"python", "java", "sql", "html", "css"}
skills_set2 = {"python", "java", "sql", "html", "css"}
common_skills = skills_set1.intersection(skills_set2)
print("Common skills between person 1 and the predefined skill set : ", common_skills)


#7. STUDENT RECORDS
print("STUDENT RECORDS :")
student_records = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 19, "grade": "A"},
    "David": {"age": 21, "grade": "C"},
    "Eve": {"age": 20, "grade": "B"}
}
print("Student records : ", student_records)
student_name = input("Enter a student name to retrieve their record : ")
if student_name in student_records:
    print(f"Record for {student_name} : {student_records[student_name]}")
else:
    print("Student not found.")
    
    
#8.MINI CONTACT BOOK
print("MINI CONTACT BOOK :")
contact_book = {
    "Alice": "+233 123 4567",
    "Bob": "+233 987 6543",
    "Charlie": "+233 555 1234"
}
print("Contact book : ", contact_book)
contact_name = input("Enter a contact name to retrieve their phone number : ")
if contact_name in contact_book:
    print(f"Phone number for {contact_name} : {contact_book[contact_name]}")
else:
    print("Contact not found.")
    
